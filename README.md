SublimeLinter-contrib-vrjasslint
================================

This linter plugin for [SublimeLinter][docs] provides an interface to [vrjasslint](https://github.com/Ruk33/vrJASS). It will be used with files that have the “__jass__” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

1. Install [SublimeLinter](http://sublimelinter.readthedocs.io/en/latest/installation.html#installing-via-pc)
2. Install [JASS Syntax Highlight](https://github.com/Ruk33/SublimeText-JASS)
3. Download this project as [ZIP](https://github.com/Ruk33/SublimeLinter-contrib-vrjasslint/archive/master.zip)
4. Go to SublimeText, Click Preferences -> Browse Packages...
5. Unzip there.
6. Restar SublimeText.

## Settings
After installation, go to SublimeText, click Preferences -> Package Settings -> SublimeLinter -> Settings - User.

If you don't have anything (or you're too lazy), paste this:

```
{
    "user": {
        "debug": true,
        "delay": 0.25,
        "error_color": "D02000",
        "gutter_theme": "none",
        "gutter_theme_excludes": [],
        "lint_mode": "background",
        "linters": {
            "vrjasslint": {
                "@disable": false,
                "args": [
                	"PATH/TO/vrjassc-jar-with-dependencies.jar",
                	"PATH/TO/common.j",
                	"PATH/TO/blizzard.j"
                ],
                "excludes": []
            }
        },
        "mark_style": "outline",
        "no_column_highlights_line": false,
        "passive_warnings": false,
        "rc_search_limit": 3,
        "shell_timeout": 10,
        "show_errors_on_save": false,
        "show_marks_in_minimap": true,
        "warning_color": "DDB700",
        "wrap_find": true
    }
}
```

delay: How much to wait before running the compiler

args: Make sure to replace the paths and Do NOT change the order!


## In action
![](http://i.imgur.com/DdEZ3fA.gif)

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
