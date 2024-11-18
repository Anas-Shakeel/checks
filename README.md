# checks

A CLI application for managing tasks for your project while coding them. It is specifically designed for programmers, but anyone can use it ofcourse.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/demo.gif" />
</p>

## Installation:

`checks` can easily be installed using `pip` package manager. (make sure python and pip are installed in your machine)

```shell
>> pip install checks-cli
```

To all non-programmers, you have to install [Python](https://www.python.org/downloads/) to use this application. _(well, atleast for now!)_

## Usage:

Run `checks` command in the terminal in your project directory _(or anywhere)_

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/checks.jpg" />
</p>

This will run the checks interactive session, similar to the Python Interactive Shell.

Now you can run commands provided by `checks`. Run `help` or `h` to see available commands.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/help.jpg" />
</p>

Seems a bit messy but it's really not. There are three columns in there. one for full **command**, one for **alias** or a shorter version, one for command **description**.

### Adding Tasks is Database / List:

Tasks can be added into list using `add` or `a` _(if you prefer less keystrokes)_.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/add_feature.jpg" />
</p>

When run for the first time, it adds a `tasks.json` in current directory and stores the task in it. After that, whenever you run `checks` in that directory and if that `tasks.json` is still there, it automatically loads that file and continues from there.

You can also add multiple tasks in one go.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/add_multiple_tasks.jpg" />
</p>

### Listing Tasks:

Now that we've added some tasks in our database, let's take a look at them using `list` or `ls` command.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/ls.jpg" />
</p>

`ls` alone, shows all tasks and their details. for a more minimal table, use the flag `-m` or `--minimal` followed by `ls`.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/ls_minimal.jpg" />
</p>

Minimal version just shows the `task` and it's `ID`. This is particularly useful in situations where you task spans multiple lines.

Apart from `-m` flag, `ls` has two more commands. `-c` or `--completed` _(which lists only completed tasks)_ and `-p` or `--pending` _(which lists only pending tasks)_.

### Checking Tasks:

You can check a task _(mark it as complete)_ using `check` or `c` command followed by Task `ID`.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/check_task.jpg" />
</p>

You can check multiple tasks at once.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/check_multiple_tasks.jpg" />
</p>

You can also use `-a` or `--all` flag which checks all pending tasks and shows how many tasks were checked.

Let's `list` the tasks now.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/check_ls.jpg" />
</p>

### Unchecking Tasks:

You can use `uncheck` or `uc` command to uncheck a task _(mark it as incomplete/pending)_.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/uncheck_task.jpg" />
</p>

Or uncheck multiple tasks.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/uncheck_multiple_tasks.jpg" />
</p>

Or uncheck all tasks.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/uncheck_all.jpg" />
</p>

Listing all tasks now.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/uncheck_ls.jpg" />
</p>

### Removing Tasks:

You can remove tasks using `remove` or `rm` command.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/rm_task.jpg" />
</p>

Or remove multiple tasks.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/rm_multiple_tasks.jpg" />
</p>

Or remove all tasks at once using `-a` or `--all` flag, following `rm`.

### Searching Tasks:

Use `search` or `s` command to search for tasks using a query/keyword. (I've added some task in database)

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/search_ls.jpg" />
</p>

Let's `search` for a tasks that contain the word **feature**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anas-Shakeel/checks/main/assets/search_feature.jpg" />
</p>

### Clearing Terminal:

By now your terminal must have been looking really messy with all the commands and outputs and the TEXT!! Well, you can clear the terminal using `clear` or `cls` command.

```shell
@checks/> clear
```

This will clear entire terminal session. Very handy!

### Saving Database:

Although `checks` saves your tasks after each successfull command execution, you can save the database manually just to be on the safe side. Use `save` or `sv` to save/write every task from in-memory database to `tasks.json`.

```shell
@checks/> save
█ Info: Database saved.
```

### Exiting Application:

Finally, Use `quit` or `q` command to quit the `checks` session.

```shell
@checks/> quit
```

Or just hit `CTRL+C` to force quit the session.

That's it. Now you know more `checks` than me, have fun coding!
