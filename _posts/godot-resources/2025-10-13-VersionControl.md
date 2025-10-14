---
layout: post
title: "Version Control"
permalink: /resources/godot/version-control
author: "Haziel Cerroblanco"
---

This page will show you step-by-step how to apply version control to your own version of the game file, and how to make sure you're up to date and are able to freely control what you're doing.

-----

## Why Version Control?
Version Control is basically a necessity if you are planning to work on either a multi-person project, or a large-scale project. It lets you save "snapshots" of your code and files which can be useful in cases where your current files break or need to be reverted. These same snapshots also allow your teammates to view and access the code you have made so that they you all have a synced workflow. 

Depending on whether you are the one setting up the project or are joining a currently existing project, there are different steps to take.

<br>

## Steps If You Are Making A New Project

1. Create a new repository in GitHub. Don't worry about giving it a good name, just make sure it's set to private (if you don't want uninvited users to access the files).
2. Open [GitHub Desktop](https://docs.github.com/en/get-started/learning-to-code/getting-started-with-git), go to the File tab, and press Clone Repository. Paste in the link of the repository you made and set the path to whatever is most convenient to you (and is always accessible).
3. Open Godot and click Create inside the Project Manager. In Project Path, toggle Create Folder *off*, and make the path the same one as step 2. Make sure Version Control Metatdata is set to Git, Then create the project as normal.

You have now linked a Godot project to GitHub! There are some more things to do, though, which can be found further below.

-----

## Steps If You Are Joining A Current Project

1. Open [GitHub Desktop](https://docs.github.com/en/get-started/learning-to-code/getting-started-with-git), go to the File tab, and press Clone Repository. Paste in the link of the project repository you are going to work on and set the path to whatever is most convenient to you (and is always accessible).
2. Open Godot and click on Import, then find the folder containing the repository and select it. The files should then be imported into the Project Manager and you can open it.

## What's Next?
Now that you have linked the repository to the Godot project files, you are able to push any changes you make into the repository.

### Commiting

<br>

### But wait, we need Branches!
In GitHub Desktop, you'll see at the top of the screen a place that says "Current Branch". In most cases, it is set to the "master" branch. Branches in Git are essentially separated environments of the same repository, where changes are independent from other branches.

The master branch is the main branch of the repository, and should contain the **finalized** changes of the game files. With that, this branch should ***not*** be actively modified. Usually, changes in the master branch are placed when a majority of the team agrees to do so. So then, what can you do?

Instead of working on the master branch, you can create your own branch where you can make non-finalized changes. To do this, click on Current Branch, and then on New Branch.

You will be given a place to put the name of your new branch (for readibility, a name such as "JohnEnvironment" is good), and then options to base your branch off of. If this is a new project, then you can just leave it on the master branch option. However, if you are joining a project that's been worked on already, you should ask your teammates on which branch would work best to be up-to-date on changes. Although, whether you choose master or not, you can always merge/pull changes into your branch when needed.

<br>

### Pulling & Merging
Whenever you want to get changes that either your peers have made in their own branches, or from the master branch (whenever it's been updated), you can use the Pull and Merge methods.

Pulling lets you fetch and merge any changes within the master branch into your current branch. It is a convenient, easy, and quick way to get new changes into your branch. To Pull from the repository, go to the Repository tab and click Pull. However, if you want more direct control over what branches to get changes from, then you can use Merge instead.

Merging allows you to specify where you want to receive changes from. With Merge, you can choose what branches you want to merge with, making it easy to get changes from specific teammates. To Merge, click on Current Branch and at the bottom click on the bottom with the text "Choose a branch to merge into JohnEnvironment". A list of branches will appear and you can choose one to merge with.

<br>

### Pushing
