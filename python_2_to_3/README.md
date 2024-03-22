
<div align="center">
<table>
<tbody>
<td align="center">
<img width="2000" height="0"><br>
<h2>Transitioning from Python 2 to Python 3</h2>
<img width="2000" height="0">
</td>
</tbody>
</table>
</div>

<p align="center">
<b>Jules Kouatchou</b> <br />
Jules.Kouatchou@nasa.gov
</p>

<p align="center">
<b>Cindy Chen</b> <br \>
Acton Boxborough Regional High School <br \>
36 Charter Rd, Acton, MA 01720 <br />
cinderellazhouchen@gmail.com 
</p>


[Website](https://github.com/astg606/astg_pymaterials/blob/main/python_2_to_3/from_python2_to_python3.ipynb) •  [Contact Us](mailto:Jules.Kouatchou@nasa.gov)

## <font color="red">Background?</font>

Python was developed in the late 1980s and first published in 1991. 

+ **Python 2** Released in 2000 to include many more programmatic features and added more features throughout its development.
+ **Python 3** Released in late 2008 and addressed and amended intrinsic design flaws. 
+ **Python 2.7** Published in 2010 as the last of the 2.x releases in order to make it easier for Python 2.x users to port features over to Python 3 by providing some measure of compatibility between the two.

Python 2.7 stopped being maintained on January 1, 2020. Python 2.6 is
no longer supported.  

> [!IMPORTANT]  
> __It is important to upgrade to Python 3.__


## <font color="red">Why Learn Python 3</font>

- Python 3 supports modern techniques like AI, Machine Learning, and Data Science
- Python 3 is supported by a large Python developer's community. Getting support is easy.
- Its easier to learn Python language compared to earlier versions.
- Offers Powerful toolkit and libraries.
- Mixable with other languages.


## <font color="red">Some Differences</font>

When getting started with porting and migration, there are several syntax changes that you can implement now.

#### `print`

The `print` statement of Python 2 has changed to a `print()` function in Python 3.

| Python 2	| Python 3 |
| --- | --- |
| `print "Hello, World!"` |	`print("Hello, World!")`|


#### Floor Division

Python 2 does floor division with the `/` operator, Python 3 introduced `//` for floor division.
Note that in Python 3, whenever two integers are divided, you get a float value whereas Python 2, you get an integer value

| Python 2	| Python 3 |
| --- | --- |
| `5 / 2 = 2` | `5 / 2 = 2.5` |
| | `5 // 2 = 2` | 

To make use of these operators in Python 2, import `division` from the `__future__` module:

```python
from __future__ import division
```

#### Integer Representation

In Python 2 the `long` type is different than the `int` type. In Python 3 the two types are the same.

| Python 2	| Python 3 |
| --- | --- |
| `123456789L` | `123456789` |
| `long(123456789)` | |

#### String Formatting

String formatting syntax has changed from Python 2 to Python 3.

| Python 2 |Python 3 |
| --- | --- |
| `"%d %s" % (i, s)` |	`"{} {}".format(i, s)` |
|                    |   `f"{i} {s}"` |
| `"%d/%d=%f" % (355, 113, 355/113)` |	`"{:d}/{:d}={:f}".format(355, 113, 355/113)` |
|                                    | `f"{355}/{113}={355/113:.f}"` |

#### `raise`

In Python 3, raising exceptions with arguments requires parentheses, and strings cannot be used as exceptions.

| Python 2 |	Python 3 |
| --- | --- |
| `raise Exception, args` |	`raise Exception` |
| | `raise Exception(args)` |
| `raise Exception, args, traceback` |	`raise Exception(args).with_traceback(traceback)` |
| `raise "Error"` |	`raise Exception("Error")` |

#### `except`

In Python 2 it was difficult to list multiple exceptions, but that has changed in Python 3.


| Python 2 |	Python 3 |
| --- | --- |
|`except Exception, variable:` |	`except AnException as variable:` |
| | `except (OneException, TwoException) as variable:` |

#### `def`

In Python 2, functions can take in sequences like tuples or lists. In Python 3, this unpacking has been removed.

| Python 2 |	Python 3 |
| --- | --- |
| `def function(arg1, (x, y)):` |	`def function(arg1, x_y): x, y = x_y` |

## <font color="red">Transitioning Process</font>

Our goal is to write codes that are both compatiple with Python 2 and Python 3.

- Start will small pieces first
- Run tests.
- Add support for Python 3 while keeping compatibility with Python 2 by introducing specific workarounds and helpers.
- Modernise your code by removing deprecated features that have a Python3-compatible equivalent available in Python 2.
- If needed, use tools to make you code both compatible with Python 2 and Python 3.

## <font color="red">A Few Tools</font>

Several tools exist to automate as much of the porting as possible, and to check for common errors. 

#### `future` 

- Works to make Python 3 idioms and best practices exist in Python 2.


Leveraging `future`, you should consider adding these `import` statements on top of each of your Python 2 modules:

```python
from __future__ import print_function
from __future__ import division
from __future__ import absolute_imports
from __future__ import unicode_literals
```

#### Compatibility Library: `six`

-  `six` module makes it practical to write code compatible with both Python 2 and 3 by offering compatibility wrappers over the differences.


#### Automated Fixer: `python-modernize`

- `python-modernize` is code-to-code translator that takes a Python 2 codebase and updates it to be compatible with both Python 2 and 3.
- The tool builds on top of `2to3`, a library that comes with Python.
- The tool operates by applying individual fixers – one for each type of change needed.

#### Automated Fixer: [2to3](https://docs.python.org/3/library/2to3.html)
- `2to3` is a Python program that utilizes the library `lib2to3` to transform Python 2 application source code into that of a Python 3 application.
- It relies on functions that detect specific syntax differences between Python 2 and Python 3, and refactor code to make it compatible with versions of Python 3.

#### Automated Checker: `pylint --py3k`

- `Pylint` is a static code analyzer that can catch mistakes such as initialized variables, unused imports, and duplicated code. 
- It also has a mode that flags code incompatible with Python 3.
- You can run the tool with the `--py3k` option on any code that is already ported. 
- You can also run pylint `--py3k` on unported code to get an idea of what will need to change.

> [!NOTE]  
> - Using an an automated tool, is a first and important step.
> - It is critical to perform tests to verify that the new code produces expected result.
> - You may need to manually rewrite sections of your codet o ensure that your Python 2 code aligns with Python 3 syntax.



## References

- [Python 2 vs Python 3: The Key Differences](https://www.mygreatlearning.com/blog/python-2-vs-python-3/) by GreatLearning
- [How to Migrate Python 2 Applications to Python 3](https://www.activestate.com/blog/how-to-migrate-python-2-applications-to-python-3/) by ActiveState
- [How To Port Python 2 Code to Python 3](https://www.digitalocean.com/community/tutorials/how-to-port-python-2-code-to-python-3) by DigitalOcean
- [The Conservative Python 3 Porting Guide](https://portingguide.readthedocs.io/en/latest/)
- [Porting Code to Python 3 with 2to3](https://diveintopython3.problemsolving.io/porting-code-to-python-3-with-2to3.html) 
- [Migrating to Python 3 with pleasure](https://github.com/arogozhnikov/python3_with_pleasure), a porting guide on features of Python 3 for data scientists
- [Moving from Python 2 to Python 3](https://ptgmedia.pearsoncmg.com/imprint_downloads/informit/promotions/python/python2python3.pdf), PDF cheatsheet for porting your Python code.

