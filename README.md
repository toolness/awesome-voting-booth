This is a simple voting booth app for [Awesome Foundation Submissions][]. Because it uses the [Twitblob API][], the whole app can be done using plain HTML files: no server-side infrastructure is required, aside from Twitblob.

Currently this app is in a very prototypical state; there are [DRY][] violations and no unit tests.

A sample instance of the app is running at [toolness.github.com][].

To modify this app for your own use, change the `load-config.js` file as needed. You can use the `pull_submissions.py` script to fill in the `submissions` key.

  [Awesome Foundation Submissions]: http://awesomefoundation.org/submissions/new
  [Twitblob API]: http://toolness.github.com/twitblob/
  [DRY]: http://en.wikipedia.org/wiki/Don't_repeat_yourself
  [tally.html]: http://github.com/toolness/awesome-voting-booth/blob/gh-pages/tally.html
  [toolness.github.com]: http://toolness.github.com/awesome-voting-booth
