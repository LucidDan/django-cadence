# Contributing to this project

## Code of Conduct

This project adheres to the Contributor Covenant code of conduct.
By participating, you are expected to uphold this code.
Please report unacceptable behavior to the [Maintainer].

## Making Contributions

Contributions from the public are welcome! You can contribute in a number of ways.

### Report Bugs

Report bugs via [GitHub Issues].
You can also report errors in documentation in this way as well.

When reporting bugs please make sure:

 1. Are you actually running up-to-date code? Make sure you have a current (supported) release or a current development version.
 2. Search and make sure someone else hasn't reported the same issue already.
 3. Include relevant details:
    1. Operating system information, including version.
    2. Deployment environment; Python? Virtualenv? Docker image? Dev or production?
    3. *Detailed* steps to reproduce the issue. As much detail as possible, please!

### Fix Bugs

If you are comfortable doing so, go through the Issues list and [create a pull request] for a bug that you think you can fix.
You can feel free to help with anything that is tagged with "bug".

See below for more information on coding style and other information relevant for contributing code to the project.

### Help add features

Help adding features is always welcome, although generally some coordination is needed in many cases.
If you are interested in working on a feature, all such Issues are tagged as "feature" - please add a comment to the Issue or contact a core developer directly to discuss it further.

### Write documentation

We could always use more documentation, whether it be adding docstrings to classes and functions in the code, or writing actual documents such as howto guides etc. The best way to go about such a thing is to create an Issue and tag it "doc", then make a pull request and get to work.
You can also search for existing "doc" Issues, there might be things we want to get done but haven't gotten around to yet.

Beyond the code itself, adding Wiki resources and expanding on README and other documentation are areas that there might be opportunities to help out on.

### Give feedback

Even if you haven't found any bugs, don't feel comfortable or capable to fix existing bugs or add features or documentation, we still appreciate feedback.

All feedback is welcome, but typically the most constructive feedback is one of the following:

 1. A detailed explanation of a new feature you think should be added.
 2. An explanation of some source of frustration or poor experience with the project.
 3. Any feedback on overall concept/architecture where you feel you have some useful input to offer.

Most problem descriptions or feature proposals should be kept specific and laser-focused.
Try to avoid grand sweeping vision features, or at least break it up into a number of smaller more consumable feature proposals.

## Code Contribution Guidelines
### Branching

We use a very simple model for branching:

 * The ```master``` branch is protected, and only code-reviewed commits that pass all integration tests can be merged (i.e. at a minimum, the code compiles).
 * ```ksp-X.Y.Z``` branches are protected, and behave exactly like master but are intended for tracking support for older KSP versions. This is mostly useful for cases where a new release requires breaking changes but we will continue to support older versions - for example when Squad changes the Unity version.
 * Other branches should generally be in forked repositories, except for projects the core maintainers are working on.
  

### Pull Request Expectations

#### One thing per PR

 * A pull request should be clean and contain commits relating only to a specific change.
 * Do not allow other changes to "leak" into your pull request, or it will be rejected.
 * Do not combine several things in one pull request that could reasonably be considered separate (either fixing different bugs, or adding different features, or whatever it might be).
 * Stick to code style conventions to avoid style change diffs to creep into your PRs.

#### Test, test, test, test

The pull request should include tests - if you aren't familiar with how to write tests in KSP mods, read up on it.

#### Documentation

If the pull request changes functionality, the documentation must be updated as well.
At a minimum, docstrings must be updated/added.
Preferably, any relevant documentation in /docs or on the Wiki should be updated or added.

### Commit Messages

[Follow the seven rules], summarised here:

1. Separate subject from body with a blank line
2. Limit the subject line to 50 characters
3. Capitalize the subject line
4. Do not end the subject line with a period
5. Use the imperative mood in the subject line
6. Wrap the body at 72 characters
7. Use the body to explain what and why vs. how

Of particular note as something that people often get wrong or forget: use present tense imperative language in (at least) the subject line. In other words:

This is preferred:

```Add a file that does this and that```

This is bad (or at the very least, not preferred):

```Added a file that does this and that```

This is AWFUL and you will go to Git hell:

```This commit is about a file, and I changed something and did this and that```

### Coding Style

TBD. In general, follow what the IDE tells you to do. ;-)


[Maintainer]: mailto:pydev@luciddan.com
[GitHub Issues]: https://github.com/LucidDan/django-cadence/issues
[Follow the seven rules]: http://chris.beams.io/posts/git-commit/#seven-rules
[create a pull request]: https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request
