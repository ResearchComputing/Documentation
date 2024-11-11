# Contributing to CURC Documentation 

At CURC we welcome all contributions. If you see something within our documentation that is not correct, can be improved, or if you have an idea for content, then [GitHub issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) are a great way to let your voice be heard and contribute to our documentation! See [Submitting an issue ](#submitting-an-issue) below for more information. Although not necessary, if you would like to personally make changes to documentation and submit them for our review, you can do this through [pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests). For more information on making pull requests and associated guidelines, please see [Submitting pull requests ](#submitting-pull-requests) below.  

## Submitting an issue 

Before creating a new issue, please review all currently open and closed issues by navigating to our [GitHub issues](https://github.com/ResearchComputing/Documentation/issues) page. If you do not see an issue that addresses your topic, you can create a new issue by first navigating to our [GitHub issues](https://github.com/ResearchComputing/Documentation/issues) page, selecting the green **"New Issue"** button, and logging in to your GitHub account.

![](./contributing_to_docs_images/creating_issue.png)

Once the new issue screen has been opened, please fill out the following two items: 
- [ ] In the **"Add a title"** section create a succinct title for your issue that clearly states what the issue is about. 
- [ ] In the **"Add a description"** section 

## Submitting pull requests 

Before creating a pull request please review 

## CURC documentation guidelines 

To ensure that our documentation is uniform and is easily digestible for users, please ensure that all documentation changes adhere to the following guidelines. 

```{note}
These guidelines are always evolving, please refer to them each time you add documentation. 
```

- [ ] Ensure that formatting and styling look good in both light and dark mode, in addition to, widescreen and mobile views of the documentation. 
- [ ] When referencing material provided in this documentation, please use an appropriate cross-reference. For more information on creating these references, please expand the drop-down box below. 
    ````{toggle} 
    By referencing documentation correctly our build scripts are able to detect broken links. To correctly reference other documentation pages or sections, please use a relative path. For example, let's say we are on the page `docs/getting_started/logging-in.md` and we want to reference the main Alpine page. To do this, we would utilize the following cross-reference: 
    ```
    [Alpine](../clusters/alpine/index.md)
    ```
    Now, let's say that we want to reference a particular heading on a page. To do this, we can append `#` along with the section title (all in lower-case, with punctuation marks removed, and spaces replaced with `-`). For example, if we are trying to reference the section **"What should I read next?"** on the Open OnDemand index page, we would do the following:
    ```
    [What should I read next?](../open_ondemand/index.md#what-should-i-read-next)
    ```
    ````
- [ ] Define any acronyms when they are first introduced.
- [ ] If there is a related topic in our documentation, link to it.
- [ ] Avoid links such as `[here]()` instead of using `here` provide a title. 
- [ ] For each new topic, provide at least a small introduction to the topic. The focus is on informing the user in a complete and clear way, not just stating information. 
- [ ] When adding images create a folder for common images and make it have the suffix `_images`. Additionally, make sure that each image is clearly labelled. 
- [ ] No file in the documentation should have spaces in the file name. Instead of using spaces `_` should be used. 
- [ ] Put all FAQs on the main FAQ page (`docs/getting_started/faq.md`). Please put the question under the appropriate section and create a section, if necessary. 
- [ ] Any reference to code filepaths, or directories should be highlighted using the code syntax i.e. the back ticks.


- [ ] Use tabs where appropriate, tabs can be really powerful and separating information so that it is more digestible for the user
- [ ] flowchart 
- [ ] admonitions 
- [ ] Use double quotes 
