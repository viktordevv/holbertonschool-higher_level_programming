<div data-target="readme-toc.content" class="Box-body px-5 pb-5">
            <article class="markdown-body entry-content container-lg" itemprop="text"><h1 dir="auto"><a id="user-content-import--modules" class="anchor" aria-hidden="true" href="#import--modules"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>import &amp; modules</h1>
<h1 dir="auto"><a id="user-content-learning-objectives" class="anchor" aria-hidden="true" href="#learning-objectives"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Learning Objectives</h1>
<ul dir="auto">
<li>How to import functions from another file</li>
<li>How to use imported functions</li>
<li>How to create a module</li>
<li>How to use the built-in function <code>dir()</code></li>
<li>How to prevent code in your script from being executed when imported</li>
<li>How to use command line arguments with your Python programs</li>
</ul>
<h1 dir="auto"><a id="user-content-tasks" class="anchor" aria-hidden="true" href="#tasks"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Tasks</h1>
<h2 dir="auto"><a id="user-content-import-a-simple-function-from-a-simple-file" class="anchor" aria-hidden="true" href="#import-a-simple-function-from-a-simple-file"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Import a simple function from a simple file</h2>
<p dir="auto">Write a program that imports the function <code>def add(a, b):</code> from the file <code>add_0.py</code> and prints the result of the addition <code>1 + 2 = 3</code></p>
<ul dir="auto">
<li>You have to use <code>print</code> function with string format to display integers</li>
<li>You have to assign:
<ul dir="auto">
<li>the value <code>1</code> to a variable called <code>a</code></li>
<li>the value <code>2</code> to a variable called <code>b</code></li>
<li>and use those two variables as arguments when calling the functions <code>add</code> and <code>print</code></li>
</ul>
</li>
<li>a and b must be defined in 2 different lines: <code>a = 1</code> and another <code>b = 2</code></li>
<li>Your program should print: <code>&lt;a value&gt; + &lt;b value&gt; = &lt;add(a, b) value&gt;</code> followed with a new line</li>
<li>You can only use the word <code>add_0</code> once in your code</li>
<li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
<li>Your code should not be executed when imported - by using <code>__import__</code>, like the example below</li>
</ul>
<p dir="auto"><strong>Solution:</strong> <a href="https://github.com/viktorkrill/holbertonschool-higher_level_programming/blob/master/0x02-python-import_modules/0-add.py">0-add.py</a></p>
<div class="snippet-clipboard-content position-relative overflow-auto"><pre class="notranslate"><code class="notranslate">$ amonkeyprogrammer@ubuntu:~/0x02$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

$ amonkeyprogrammer@ubuntu:~/0x02$ ./0-add.py
1 + 2 = 3
$ amonkeyprogrammer@ubuntu:~/0x02$ cat 0-import_add.py
__import__("0-add")
$ amonkeyprogrammer@ubuntu:~/0x02$ python3 0-import_add.py 
$ amonkeyprogrammer@ubuntu:~/0x02$
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ amonkeyprogrammer@ubuntu:~/0x02$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    &quot;&quot;&quot;My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    &quot;&quot;&quot;
    return (a + b)

$ amonkeyprogrammer@ubuntu:~/0x02$ ./0-add.py
1 + 2 = 3
$ amonkeyprogrammer@ubuntu:~/0x02$ cat 0-import_add.py
__import__(&quot;0-add&quot;)
$ amonkeyprogrammer@ubuntu:~/0x02$ python3 0-import_add.py 
$ amonkeyprogrammer@ubuntu:~/0x02$" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<h2 dir="auto"><a id="user-content-my-first-toolbox" class="anchor" aria-hidden="true" href="#my-first-toolbox"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>My first toolbox!</h2>
<p dir="auto">Write a program that imports functions from the file <code>calculator_1.py</code>, does some Maths, and prints the result.</p>
<ul dir="auto">
<li>Do not use the function <code>print</code> (with string format to display integers) more than 4 times</li>
<li>You have to define:
<ul dir="auto">
<li>the value <code>10</code> to a variable <code>a</code></li>
<li>the value <code>5</code> to a variable <code>b</code></li>
<li>and use those two variables only, as arguments when calling functions (including <code>print</code>)</li>
</ul>
</li>
<li><code>a</code> and <code>b</code> must be defined in 2 different lines: <code>a = 10</code> and another <code>b = 5</code></li>
<li>Your program should call each of the imported functions. See example below for format</li>
<li>the word <code>calculator_1</code> should be used only once in your file</li>
<li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
<li>Your code should not be executed when imported</li>
</ul>
<p dir="auto"><strong>Solution:</strong> <a href="https://github.com/viktorkrill/holbertonschool-higher_level_programming/blob/master/0x02-python-import_modules/1-calculation.py">1-calculation.py</a></p>
<div class="snippet-clipboard-content position-relative overflow-auto"><pre class="notranslate"><code class="notranslate">$ amonkeyprogrammer@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

$ amonkeyprogrammer@ubuntu:~/0x02$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
$ amonkeyprogrammer@ubuntu:~/0x02$
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ amonkeyprogrammer@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    &quot;&quot;&quot;My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    &quot;&quot;&quot;
    return (a + b)


def sub(a, b):
    &quot;&quot;&quot;My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    &quot;&quot;&quot;
    return (a - b)


def mul(a, b):
    &quot;&quot;&quot;My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    &quot;&quot;&quot;
    return (a * b)


def div(a, b):
    &quot;&quot;&quot;My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    &quot;&quot;&quot;
    return int(a / b)

$ amonkeyprogrammer@ubuntu:~/0x02$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
$ amonkeyprogrammer@ubuntu:~/0x02$" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<h2 dir="auto"><a id="user-content-how-to-make-a-script-dynamic" class="anchor" aria-hidden="true" href="#how-to-make-a-script-dynamic"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>How to make a script dynamic!</h2>
<p dir="auto">Write a program that prints the number of and the list of its arguments.</p>
<ul dir="auto">
<li>The output should be:
<ul dir="auto">
<li>Number of argument(s) followed by <code>argument</code> (if number is one) or <code>arguments</code> (otherwise), followed by</li>
<li><code>:</code> (or <code>.</code> if no arguments were passed) followed by</li>
<li>a new line, followed by (if at least one argument),</li>
<li>one line per argument:
<ul dir="auto">
<li>the position of the argument (starting at <code>1</code>) followed by <code>:</code>, followed by the argument value and a new line</li>
</ul>
</li>
</ul>
</li>
<li>Your code should not be executed when imported</li>
<li>The number of elements of <code>argv</code> can be retrieved by using: <code>len(argv)</code></li>
<li>You do not have to fully understand lists yet, but imagine that <code>argv</code> can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.</li>
</ul>
<p dir="auto"><strong>Solution:</strong> <a href="https://github.com/viktorkrill/holbertonschool-higher_level_programming/blob/master/0x02-python-import_modules/2-args.py">2-args.py</a></p>
<div class="snippet-clipboard-content position-relative overflow-auto"><pre class="notranslate"><code class="notranslate">$ amonkeyprogrammer@ubuntu:~/0x02$ ./2-args.py 
0 arguments.
$ amonkeyprogrammer@ubuntu:~/0x02$ ./2-args.py Hello
1 argument:
1: Hello
$ amonkeyprogrammer@ubuntu:~/0x02$ ./2-args.py Hello Holberton School 98 Battery street
6 arguments:
1: Hello
2: Holberton
3: School
4: 98
5: Battery
6: street
$ amonkeyprogrammer@ubuntu:~/0x02$
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ amonkeyprogrammer@ubuntu:~/0x02$ ./2-args.py 
0 arguments.
$ amonkeyprogrammer@ubuntu:~/0x02$ ./2-args.py Hello
1 argument:
1: Hello
$ amonkeyprogrammer@ubuntu:~/0x02$ ./2-args.py Hello Holberton School 98 Battery street
6 arguments:
1: Hello
2: Holberton
3: School
4: 98
5: Battery
6: street
$ amonkeyprogrammer@ubuntu:~/0x02$" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<h2 dir="auto"><a id="user-content-infinite-addition" class="anchor" aria-hidden="true" href="#infinite-addition"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Infinite addition</h2>
<p dir="auto">Write a program that prints the result of the addition of all arguments</p>
<ul dir="auto">
<li>The output should be the result of the addition of all arguments, followed by a new line</li>
<li>You can cast arguments into integers by using <code>int()</code> (you can assume that all arguments can be casted into integers)</li>
<li>Your code should not be executed when imported</li>
</ul>
<div class="snippet-clipboard-content position-relative overflow-auto"><pre class="notranslate"><code class="notranslate">$ amonkeyprogrammer@ubuntu:~/0x02$ ./3-infinite_add.py
0
$ amonkeyprogrammer@ubuntu:~/0x02$ ./3-infinite_add.py 79 10
89
$ amonkeyprogrammer@ubuntu:~/0x02$ ./3-infinite_add.py 79 10 -40 -300 89 
-162
$ amonkeyprogrammer@ubuntu:~/0x02$
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ amonkeyprogrammer@ubuntu:~/0x02$ ./3-infinite_add.py
0
$ amonkeyprogrammer@ubuntu:~/0x02$ ./3-infinite_add.py 79 10
89
$ amonkeyprogrammer@ubuntu:~/0x02$ ./3-infinite_add.py 79 10 -40 -300 89 
-162
$ amonkeyprogrammer@ubuntu:~/0x02$" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto">Last but not least, your program should also handle big numbers. And the good news is: if your program works for the above example, it will work for the following example:</p>
<p dir="auto"><strong>Solution:</strong> <a href="https://github.com/viktorkrill/holbertonschool-higher_level_programming/blob/master/0x02-python-import_modules/3-infinite_add.py">3-infinite_add.py</a></p>
<div class="snippet-clipboard-content position-relative overflow-auto"><pre class="notranslate"><code class="notranslate">$ amonkeyprogrammer@ubuntu:~/0x02$ ./3-infinite_add.py 1111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999990000000000000000000 11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334567788888899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334568900000011111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999989999999999999999999
$ amonkeyprogrammer@ubuntu:~/0x02$
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ amonkeyprogrammer@ubuntu:~/0x02$ ./3-infinite_add.py 1111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999990000000000000000000 11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334567788888899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334568900000011111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999989999999999999999999
$ amonkeyprogrammer@ubuntu:~/0x02$" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<h2 dir="auto"><a id="user-content-who-are-you" class="anchor" aria-hidden="true" href="#who-are-you"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Who are you?</h2>
<p dir="auto">Write a program that prints all the names defined by the compiled module <a href="https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc">hidden_4.pyc</a></p>
<ul dir="auto">
<li>You should print one name per line, in alpha order</li>
<li>You should print only names that do <strong>not</strong> start with <code>__</code></li>
<li>Your code should not be executed when imported</li>
<li>Make sure you are running your code in Python3.4.x (<code>hidden_4.pyc</code> has been compiled with this version)</li>
</ul>
<p dir="auto"><strong>Solution:</strong> <a href="https://github.com/viktorkrill/holbertonschool-higher_level_programming/blob/master/0x02-python-import_modules/4-hidden_discovery.py">4-hidden_discovery.py</a></p>
<div class="snippet-clipboard-content position-relative overflow-auto"><pre class="notranslate"><code class="notranslate">$ amonkeyprogrammer@ubuntu:~/0x02$ curl -Lso "hidden_4.pyc" "https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc"
$ amonkeyprogrammer@ubuntu:~/0x02$ ./4-hidden_discovery.py | sort
my_secret_santa
print_holberton
print_school
$ amonkeyprogrammer@ubuntu:~/0x02$
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ amonkeyprogrammer@ubuntu:~/0x02$ curl -Lso &quot;hidden_4.pyc&quot; &quot;https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc&quot;
$ amonkeyprogrammer@ubuntu:~/0x02$ ./4-hidden_discovery.py | sort
my_secret_santa
print_holberton
print_school
$ amonkeyprogrammer@ubuntu:~/0x02$" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<h2 dir="auto"><a id="user-content-everything-can-be-imported" class="anchor" aria-hidden="true" href="#everything-can-be-imported"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Everything can be imported</h2>
<p dir="auto">Write a program that imports the variable <code>a</code> from the file <code>variable_load_5.py</code> and prints its value.</p>
<ul dir="auto">
<li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
<li>Your code should not be executed when imported</li>
</ul>
<p dir="auto"><strong>Solution:</strong> <a href="https://github.com/viktorkrill/holbertonschool-higher_level_programming/blob/master/0x02-python-import_modules/5-variable_load.py">5-variable_load.py</a></p>
<div class="snippet-clipboard-content position-relative overflow-auto"><pre class="notranslate"><code class="notranslate">$ amonkeyprogrammer@ubuntu:~/0x02$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
"""Simple variable
"""

$ amonkeyprogrammer@ubuntu:~/0x02$ ./5-variable_load.py
98
$ amonkeyprogrammer@ubuntu:~/0x02$
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ amonkeyprogrammer@ubuntu:~/0x02$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
&quot;&quot;&quot;Simple variable
&quot;&quot;&quot;

$ amonkeyprogrammer@ubuntu:~/0x02$ ./5-variable_load.py
98
$ amonkeyprogrammer@ubuntu:~/0x02$" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<h2 dir="auto"><a id="user-content-build-my-own-calculator" class="anchor" aria-hidden="true" href="#build-my-own-calculator"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Build my own calculator!</h2>
<p dir="auto">Write a program that imports all functions from the file <code>calculator_1.py</code> and handles basic operations.</p>
<ul dir="auto">
<li>Usage: <code>./100-my_calculator.py a operator b</code>
<ul dir="auto">
<li>If the number of arguments is not 3, your program has to:
<ul dir="auto">
<li>print <code>Usage: ./100-my_calculator.py &lt;a&gt; &lt;operator&gt; &lt;b&gt;</code> followed with a new line</li>
<li>exit with the value 1</li>
</ul>
</li>
<li><code>operator</code> can be:
<ul dir="auto">
<li><code>+</code> for addition</li>
<li><code>-</code> for subtraction</li>
<li><code>*</code> for multiplication</li>
<li><code>/</code> for division</li>
</ul>
</li>
<li>If the operator is not one of the above:
<ul dir="auto">
<li>print <code>Unknown operator. Available operators: +, -, * and /</code> followed with a new line</li>
<li>exit with the value <code>1</code></li>
</ul>
</li>
<li>You can cast <code>a</code> and <code>b</code> into integers by using <code>int()</code> (you can assume that all arguments will be castable into integers)</li>
<li>The result should be printed like this: <code>&lt;a&gt; &lt;operator&gt; &lt;b&gt; = &lt;result&gt;</code>, followed by a new line</li>
</ul>
</li>
<li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
<li>Your code should not be executed when imported</li>
</ul>
<p dir="auto"><strong>Solution:</strong> <a href="https://github.com/viktorkrill/holbertonschool-higher_level_programming/blob/master/0x02-python-import_modules/100-my_calculator.py">100-my_calculator.py</a></p>
<div class="snippet-clipboard-content position-relative overflow-auto"><pre class="notranslate"><code class="notranslate">$ amonkeyprogrammer@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

$ amonkeyprogrammer@ubuntu:~/0x02$ ./100-my_calculator.py ; echo $?
Usage: ./100-my_calculator.py &lt;a&gt; &lt;operator&gt; &lt;b&gt;
1
$ amonkeyprogrammer@ubuntu:~/0x02$ ./100-my_calculator.py 3 + 5 ; echo $?
3 + 5 = 8
0
$ amonkeyprogrammer@ubuntu:~/0x02$ ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
1
$ amonkeyprogrammer@ubuntu:~/0x02$
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ amonkeyprogrammer@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    &quot;&quot;&quot;My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    &quot;&quot;&quot;
    return (a + b)


def sub(a, b):
    &quot;&quot;&quot;My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    &quot;&quot;&quot;
    return (a - b)


def mul(a, b):
    &quot;&quot;&quot;My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    &quot;&quot;&quot;
    return (a * b)


def div(a, b):
    &quot;&quot;&quot;My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    &quot;&quot;&quot;
    return int(a / b)

$ amonkeyprogrammer@ubuntu:~/0x02$ ./100-my_calculator.py ; echo $?
Usage: ./100-my_calculator.py <a> <operator> <b>
1
$ amonkeyprogrammer@ubuntu:~/0x02$ ./100-my_calculator.py 3 + 5 ; echo $?
3 + 5 = 8
0
$ amonkeyprogrammer@ubuntu:~/0x02$ ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
1
$ amonkeyprogrammer@ubuntu:~/0x02$" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<h2 dir="auto"><a id="user-content-easy-print" class="anchor" aria-hidden="true" href="#easy-print"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Easy print</h2>
<p dir="auto">Write a program that prints <code>#pythoniscool</code>, followed by a new line, in the standard output.</p>
<ul dir="auto">
<li>Your program should be maximum 2 lines long</li>
<li>You are not allowed to use <code>print</code> or <code>eval</code> or <code>open</code> or <code>import sys</code> in your file <code>101-easy_print.py</code></li>
</ul>
<p dir="auto"><strong>Solution:</strong> <a href="https://github.com/viktorkrill/holbertonschool-higher_level_programming/blob/master/0x02-python-import_modules/101-easy_print.py">101-easy_print.py</a></p>
<div class="snippet-clipboard-content position-relative overflow-auto"><pre class="notranslate"><code class="notranslate">$ amonkeyprogrammer@ubuntu:~/0x02$ ./101-easy_print.py
#pythoniscool
$ amonkeyprogrammer@ubuntu:~/0x02$
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ amonkeyprogrammer@ubuntu:~/0x02$ ./101-easy_print.py
#pythoniscool
$ amonkeyprogrammer@ubuntu:~/0x02$" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<h2 dir="auto"><a id="user-content-bytecode---python-3" class="anchor" aria-hidden="true" href="#bytecode---python-3"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>ByteCode -&gt; Python #3</h2>
<p dir="auto">Write the Python function <code>def magic_calculation(a, b):</code> that does exactly the same as the following Python bytecode:</p>
<p dir="auto"><strong>Solution:</strong> <a href="https://github.com/viktorkrill/holbertonschool-higher_level_programming/blob/master/0x02-python-import_modules/102-magic_calculation.py">102-magic_calculation.py</a></p>
<div class="snippet-clipboard-content position-relative overflow-auto"><pre class="notranslate"><code class="notranslate">  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (&lt;)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        &gt;&gt;   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        &gt;&gt;   89 POP_BLOCK

  8     &gt;&gt;   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     &gt;&gt;   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w" value="  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<h2 dir="auto"><a id="user-content-fast-alphabet" class="anchor" aria-hidden="true" href="#fast-alphabet"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Fast alphabet</h2>
<p dir="auto">Write a program that prints the alphabet in uppercase, followed by a new line.</p>
<ul dir="auto">
<li>Your program should be maximum 3 lines long</li>
<li>You are not allowed to use:
<ul dir="auto">
<li>any loops</li>
<li>any conditional statements</li>
<li><code>str.join()</code></li>
<li>any string literal</li>
<li>any system calls</li>
</ul>
</li>
</ul>
<p dir="auto"><strong>Solution:</strong> <a href="https://github.com/viktorkrill/holbertonschool-higher_level_programming/blob/master/0x02-python-import_modules/103-fast_alphabet.py">103-fast_alphabet.py</a></p>
<div class="snippet-clipboard-content position-relative overflow-auto"><pre class="notranslate"><code class="notranslate">$ amonkeyprogrammer@ubuntu:~/0x02$ ./103-fast_alphabet.py
ABCDEFGHIJKLMNOPQRSTUVWXYZ
$ amonkeyprogrammer@ubuntu:~/0x02$ wc -l 103-fast_alphabet.py
3 103-fast_alphabet.py
$ amonkeyprogrammer@ubuntu:~/0x02$
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ amonkeyprogrammer@ubuntu:~/0x02$ ./103-fast_alphabet.py
ABCDEFGHIJKLMNOPQRSTUVWXYZ
$ amonkeyprogrammer@ubuntu:~/0x02$ wc -l 103-fast_alphabet.py
3 103-fast_alphabet.py
$ amonkeyprogrammer@ubuntu:~/0x02$" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    </clipboard-copy>
  </div></div>
</article>
          </div>