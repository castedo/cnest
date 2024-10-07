The Cnest Guide to Personal Multisession Containers
===================================================

<img src="_static/bird-nest-260px.png"
 style="height: 192px; float:right;"
 alt="Bird Nest">

Why this guide
--------------

This guide will show you how to use [Podman](https://podman.io) and small wrapper bash
scripts to create personalized Linux containers for concurrent interactive shell
sessions.
Before getting started, consider some reasons you might, or might not, want to use this
guide.

### Some reasons to use this guide

* You work in interactive shell sessions with CLI software.
* You want to be able to install software in isolated environments without interfering
  with your host computer.
* You want to use CLI software on a variety of Linux distributions.
* You like to control what access your isolated environment has to your system.
* You want to have a lot of control over how you set up and personalize your setup.
* You sometimes write small bash scripts (or similar).

If this sounds like you, then [let's get started with Podman](podman.md).

### Some reasons to NOT use this guide

* If you are trying to run a GUI application that is NOT packaged for your Linux distro.
* If you want installed software to have access to all of your desktop environment.
* If you want an isolation approach that also works without Linux.

If any of these is your main objective, skip to the [part of this guide about
alternative approaches](other-tools.md).


Feedback
--------

If you have any suggestions or additions for this guide, you can edit these pages or
[start a discussion](https://github.com/castedo/cnest/discussions) on GitHub.
If you have any issues or feedback for the cnest package, [submit an
issue](https://github.com/castedo/cnest/issues) or email
[Castedo](mailto:castedo@castedo.com).
