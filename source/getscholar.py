
import scholarly
import markdown2
import os
import json
import pprint

CONTENT = "content"

def path_to_md(base, filename):
    md_path = os.path.join(CONTENT, base)
    md = markdown2.markdown_path(os.path.join(md_path, filename), extras=["metadata"])
    md.filename = os.path.splitext(filename)[0]
    return md


def get_mds(base):
    files = [f for f in os.listdir(os.path.join(CONTENT, base)) if f.lower().endswith(".md")]
    mds = [path_to_md(base, f) for f in files]
    return mds


def get_scholars():
    mds = get_mds('people')
    return [md.metadata['scholar'] for md in mds if 'scholar' in md.metadata]


def get_paper(pub):
    print(f":: {pub.bib['title']}")
    pub.fill() # takes extra time
    if 'abstract' in pub.bib and not type(pub.bib['abstract']) is str:
        pub.bib['abstract'] = pub.bib['abstract'].text
    if 'eprint' in pub.bib:
        pub.bib['eprint'] = pub.bib['eprint'].replace("https://scholar.google.com", "")

    return pub.bib


def get_papers(author):
    author.fill()
    print(f"fetching papers from {author.name}")
    pubs = [get_paper(pub) for pub in author.publications]
    pubs_sorted = {}
    for pub in pubs:
        year = pub.get('year', 0) # magic number "0" indicates undated
        if year == 1970:
            pub['year'] = 0
            year = 0
        if year not in pubs_sorted:
            pubs_sorted[year] = []
        pubs_sorted[year].append(pub)
    return pubs_sorted


def get_page_overload(pagerequest):
    """
    Overload for default _get_page function in scholarly 
    """
    resp = scholarly._SESSION.get(pagerequest, headers=scholarly._HEADERS, cookies=scholarly._COOKIES)
    if resp.status_code == 200:
        return resp.text
    if resp.status_code == 503:
        raise Exception('Error: {0} {1}'.format(resp.status_code, resp.reason))
    else:
        raise Exception('Error: {0} {1}'.format(resp.status_code, resp.reason))

scholarly._get_page = get_page_overload


if __name__ == "__main__":
    scholars = get_scholars()
    authors = {s: scholarly.Author(s) for s in scholars}
    papers = {s: get_papers(a) for s, a in authors.items()}
    with open(os.path.join(CONTENT, 'papers.json'), 'w+', encoding="utf-8") as f:
        print(f"papers info saved to papers.json")
        json.dump(papers, f, indent=2, ensure_ascii=False, skipkeys=True)
    scholarly._SESSION.__exit__()