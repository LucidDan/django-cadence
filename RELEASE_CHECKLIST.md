# Release Checklist

Things that need to be completed and should be checked before each release is made:

 1. Check to make sure [tox.ini] and [.travis.yml] include all currently supported Python and Django releases.
 2. Check to make sure that the supported releases documented in [SECURITY.md] and in [README.md] is up-to-date.
 2. Check all tests are passing. 
 3. Documentation is updated.
 4. Update [CHANGELOG.md]:
   a) Section has been created for the release version, usually by renaming "Unreleased" and creating a new "Unreleased".
   b) Links are updated, especially for linking to version number.
 5. Make sure the "What's New" section in [README.md] is updated to the new release.
 6. Tag the release and create a pull request for it.
 7. Verify that the release appears on GitHub releases and on pypi.
 8. Sanity check: make sure the new pypi release can be installed and works.
