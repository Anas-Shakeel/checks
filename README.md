# checks

A CLI application for managing tasks for your project while coding them. It is specifically designed for programmers, but anyone can use it ofcourse.

## Setup and Installation:

`checks` can easily be installed using `pip` package manager. (make sure python and pip are installed in your machine)

```shell
>> pip install checks-cli
```

## Usage:

Run `checks` command in the terminal in your project directory (or anywhere)

```shell
>> checks
Checks 1.1.0
Type 'help' for usage hint. (CTRL+C to force quit)

@checks/>
```

This will run the checks interactive session, similar to the Python Interactive Shell.

Now you can run commands provided by `checks`. Run `help` or `h` to see available commands.

```shell
@checks/> help
add,     a       add tasks
check,   c       mark tasks as complete
uncheck, uc      mark tasks as incomplete
remove,  rm      remove tasks
list,    ls      list all tasks
search,  s       search tasks
clear,   cls     clear terminal
save,    sv      save all tasks
quit,    q       exit the application
help,    h       print this help text
```

Seems a bit messy but it's really not. There are three columns in there. one for full command, one for alias or a shorter version, one for command descriptions.

### Adding Tasks is Database / List:

Tasks can be added into list using `add` or `a` _(if you prefer less keystrokes)_.

```shell
@checks/> add "This is the first task in the list."
█ Info: 'This is the first task in the list.' added.
```

When run for the first time, it adds a `tasks.json` in current directory and stores the task in it. After that, whenever you run `checks` in that directory and if that `tasks.json` is still there, it automatically loads that file and continues from there.

You can also add multiple tasks in one go.

```shell
@checks/> add "Task 1", "Task 2", "Task N"
█ Info: 3 Tasks added.
```

### Listing Tasks:

Now that we've added some tasks in our database, let's take a look at them using `list` or `ls` command.

```shell
@checks/> ls
┌──────┬─────────────────────────────────────┬──────────┬────────────────┐
│   Id │ Description                         │ Status   │ Created        │
├──────┼─────────────────────────────────────┼──────────┼────────────────┤
│    1 │ This is the first task in the list. │ Pending  │ 13 minutes ago │
│    2 │ Task 1                              │ Pending  │ 1 minute ago   │
│    3 │ Task 2                              │ Pending  │ 1 minute ago   │
│    4 │ Task N                              │ Pending  │ 1 minute ago   │
└──────┴─────────────────────────────────────┴──────────┴────────────────┘
```

`ls` alone, shows all tasks and their details. for a more minimal table, use the flag `-m` or `--minimal` followed by `ls`.

```shell
@checks/> ls -m
1  This is the first task in the list.
2  Task 1
3  Task 2
4  Task N
```

Minimal version just shows the `task` and it's `ID`. This is particularly useful in situations where you task spans multiple lines.

Apart from `-m` flag, `ls` has two more commands. `-c` or `--completed` _(which lists only completed tasks)_ and `-p` or `--pending` _(which lists only pending tasks)_.

### Checking Tasks:

You can check a task _(mark it as complete)_ using `check` or `c` command followed by Task `ID`.

```shell
@checks/> check 1
█ Info: 'This is the first task in the list.' checked.
```

You can check multiple tasks at once.

```shell
@checks/> check 2, 3
█ Info: 2 Tasks checked.
```

You can also check all tasks using `-a` or `--all` flag.

```shell
@checks/> check -a
█ Info: 1 Tasks checked.
```

It checks all pending tasks and shows how many tasks were checked.

Let's `list` the tasks now.

```shell
@checks/> ls
┌──────┬─────────────────────────────────────┬───────────┬────────────────┐
│   Id │ Description                         │ Status    │ Created        │
├──────┼─────────────────────────────────────┼───────────┼────────────────┤
│    1 │ This is the first task in the list. │ Completed │ 35 minutes ago │
│    2 │ Task 1                              │ Completed │ 23 minutes ago │
│    3 │ Task 2                              │ Completed │ 23 minutes ago │
│    4 │ Task N                              │ Completed │ 23 minutes ago │
└──────┴─────────────────────────────────────┴───────────┴────────────────┘
```

### Unchecking Tasks:

You can use `uncheck` or `uc` command to uncheck a task _(mark it as incomplete/pending)_.

```shell
@checks/> uncheck 2
█ Info: 'Task 1' unchecked.
```

Or uncheck multiple tasks.

```shell
@checks/> uc 3, 4
█ Info: 2 Tasks unchecked.
```

Or uncheck all tasks.

```shell
@checks/> uc -a
█ Info: 1 Tasks unchecked.
```

Listing all tasks now.

```shell
@checks/> ls
┌──────┬─────────────────────────────────────┬──────────┬────────────────┐
│   Id │ Description                         │ Status   │ Created        │
├──────┼─────────────────────────────────────┼──────────┼────────────────┤
│    1 │ This is the first task in the list. │ Pending  │ 52 minutes ago │
│    2 │ Task 1                              │ Pending  │ 41 minutes ago │
│    3 │ Task 2                              │ Pending  │ 41 minutes ago │
│    4 │ Task N                              │ Pending  │ 41 minutes ago │
└──────┴─────────────────────────────────────┴──────────┴────────────────┘
```

### Removing Tasks:

You can remove tasks using `remove` or `rm` command.

```shell
@checks/> rm 4
█ Info: 'Task N' removed.
```

Or remove multiple tasks.

```shell
@checks/> rm 2, 3
█ Info: 2 Tasks removed.
```

Or remove all tasks at once using `-a` or `--all` flag, following `rm`.

### Searching Tasks:

Use `search` or `s` command to search for tasks using a query/keyword. (I've added some task in database)

```shell
@checks/> ls
┌──────┬─────────────────────────────────────────────────┬──────────┬───────────────┐
│   Id │ Description                                     │ Status   │ Created       │
├──────┼─────────────────────────────────────────────────┼──────────┼───────────────┤
│    1 │ This is the first task in the list.             │ Pending  │ 4 hours ago   │
│    2 │ Add search feature in checks.                   │ Pending  │ 2 seconds ago │
│    3 │ Fix that bug thats bugging you for a long time. │ Pending  │ 2 seconds ago │
│    4 │ Update README                                   │ Pending  │ 2 seconds ago │
└──────┴─────────────────────────────────────────────────┴──────────┴───────────────┘
```

Let's `search` for a tasks that contain the word **feature**.

```shell
@checks/> s "feature"
┌──────┬───────────────────────────────┬──────────┬───────────────┐
│   Id │ Description                   │ Status   │ Created       │
├──────┼───────────────────────────────┼──────────┼───────────────┤
│    2 │ Add search feature in checks. │ Pending  │ 6 minutes ago │
└──────┴───────────────────────────────┴──────────┴───────────────┘
```

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
