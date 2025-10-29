# 这行代码指定了CMake的最低版本要求，即使用此CMakeLists.txt文件时，CMake的版本至少需要是3.8。这是为了确保项目在构建时所使用的CMake版本具备支持后续指令的能力。
cmake_minimum_required(VERSION 3.8)     
# 这行代码定义了项目的名称为hello。项目名称在构建过程中主要用于生成相关文件和目录时的默认命名，比如可执行文件、库文件等。
project(hello)
# 这行代码用于添加一个可执行文件的目标，目标名称为learn_cmake，它将根据指定的源文件hello.cpp进行构建。这里的意思是，CMake会根据hello.cpp的代码内容来编译生成一个名为learn_cmake的可执行程序。
add_executable(learn_cmake hello.cpp)
