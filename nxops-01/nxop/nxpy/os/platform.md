`import platform` 是Python中的另一个语句，用于导入`platform`模块。`platform`模块提供了许多用于访问底层平台（即操作系统）信息的函数。

当你使用`import platform`导入这个模块后，你可以使用它来获取关于运行Python解释器的系统的详细信息，例如操作系统名称、版本、发行版、处理器架构等。

以下是一些`platform`模块中常用的函数：

1. **获取操作系统信息**：
   - `platform.system()`: 返回操作系统的名称，例如'Linux'、'Windows'或'Darwin'（对于macOS）。
   - `platform.release()`: 返回操作系统的发行版信息。
   - `platform.version()`: 返回操作系统的版本信息。
   - `platform.platform()`: 返回描述当前平台的字符串，这通常包含操作系统名称、版本和发行版信息。

2. **获取硬件信息**：
   - `platform.machine()`: 返回机器硬件名称，如'x86_64'、'i686'等。
   - `platform.processor()`: 返回CPU的体系结构，例如'x86_64'。

3. **获取Python解释器信息**：
   - `platform.python_version()`: 返回Python解释器的版本信息。
   - `platform.python_compiler()`: 返回用来编译Python解释器的编译器的名称。
   - `platform.python_build()`: 返回一个包含构建日期和时间以及编译器的元组。

4. **其他信息**：
   - `platform.uname()`: 返回一个包含多种平台信息的命名元组，类似于Unix的`uname`命令。
   - `platform.node()`: 返回网络节点上的计算机名称。

这些函数可以帮助你编写跨平台的代码，因为你可以根据获取到的平台信息来执行不同的操作或提供不同的功能。

例如，你可能需要为不同的操作系统使用不同的文件路径分隔符，或者你可能需要根据处理器的架构来选择不同的二进制文件。通过使用`platform`模块，你可以以编程方式获取这些信息，而不是硬编码它们。