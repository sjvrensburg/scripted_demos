# scripted_demos

Simple tool along the lines of [asciicast](https://github.com/r-lib/asciicast). The script takes a file and types the content of that file into whatever window has focus.

## Installation

**Any tool that "takes over" your keyboard poses a security risk.** Rather than install `scripted_demo`, I recommend using `pipx run` as follows:

```bash
pipx run --spec git+https://github.com/sjvrensburg/scripted_demos demo -c start -d 5 input.R
```

This will:

1. download and install `scripted_demos` into a temporary virtual environment,
2. run the command `demo`, which
3. waits for you to type `start` and press enter, then
4. waits five seconds fore 
5. it starts to type the contents of the file `input.R` into the focused window.

Note that `pipx run` creates a one-time, temporary environment, leaving your system untouched afterwards.

## Arguments

### `-c` or `--cmd`

The trigger phrase to watch out for. This can be a command, such `R` or `bpython`, or it can be a word like `start`. After typing the trigger phrase and pressing enter, the script will start reading the specified file.

### `-d` or `--delay`

How many seconds to wait after receiving the trigger phrase before the app starts typing the contents of the file. The delay gives you time to place the focus on the correct window.

### `input`

The file to read and type out. You can think of this as the "script" to your code demonstration. This "script" can contain special commands that will affect how the app types the commands.

## Special Commands Inside `input`

The app reads the file line-by-line. If the line starts with a special command then it changes how the app outputs that line to the active window.

The commands are as follows:

- `#!!` wait for the user to press enter,
- `#<< some text` will output `# some text` to the active window without any delays,
- `#cls` will simulate the keyboard command `ctrl+l`, which clears the screen in most programs and
- `#{5}` will pause for 5 seconds (replace 5 with how many seconds you want to pause).

## Tips And Tricks

If you are going to use this to type commands into RStudio, disable the global option to insert matching parentheses and quotes.

Also, keep the console from which you launched the app visible. It will show you what the next line in your file and alert you when the app is waiting for user input.
