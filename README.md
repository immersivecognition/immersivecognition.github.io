# immersivecognition.github.io
Immersive Cognition GitHub landing page

## Information

Website is built in Flask (Python module). The static HTML content is generated using Frozen-Flask.

## Updating (for users)

Users can add/modify markdown files in the [/source/content/people](/source/content/people) or [/source/content/projects](/source/content/projects) and submit as a pull request. See existing markdown files for examples

* ```email``` must just be the username (i.e. with `@leeds.ac.uk` removed)
* ```scholar``` is the code/ID in the URL of your Google Scholar profile (e.g. in ```0kwtpyoAAAAJ``` in ```...citations?user=0kwtpyoAAAAJ&hl=en```)
* ```twitter``` and ```github``` are optional and are just usernames (not the full URL)
* ```interests``` are a list of interests each separated by a comma.

Images can also be placed in [/source/content/people-images](/source/content/people-images) or [/source/content/project-images](/source/content/project-images), and referenced as `person.jpg` or `project.png` (images will automatically cropped to a square and converted to jpg and png for people and projects respectively). 

To add/remove/modify papers, don't edit `papers.json` directly - instead fix the papers on your Google Scholar profile and the changes will be added the next time the website is rebuilt.


## Updating (for developers)

If users add content (markdown files, or images), the developer needs to [clone the pull request](https://help.github.com/articles/checking-out-pull-requests-locally/). With the local repository run the following Python scripts (from the `/source` folder to incorporate the changes into the static HTML:

### Resizing the images

    python resizeimg.py
    
This will crop and convert the images and move them to the Flask app's static files directory.

### Fetching articles from Google Scholar

    python getscholar.py

This will fetch metadata for every article for each person that has provided a Scholar ID. It then stores the metadata in ```papers.json``` overwriting the existing file. This will take a while.

### Testing

    python application.py

This generates a local server so you can test the website locally in a web browser

### Building the website

    python freeze.py
    
This walks over every link, and generates the static HTML for each page. 

### Publishing

When you are happy with the changes, you can commit and push the changes to this repository.
