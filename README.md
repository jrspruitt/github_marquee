Print a short message to the github commit calendar

To run, create github repo

clone this repo

    # cd github_marquee/
    # rm -rf .git/
    # git init
    # git add .
    # git remote add origin <your github repo>
    # ./github_marquee.py <message>
    # git push origin master --force

Be sure to force it as it'll complain.

To adjust the start, change c in git\_marquee.py after the main if.
This will move it over c number of characters, which is 4 colums.

You only get once chance that I can tell, to change it you'll need to delete the repo, and recreate it.
