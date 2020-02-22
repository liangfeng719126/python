//
//  test_cpy_model.c
//  tpytest
//
//  Created by 梁丰 on 2020/2/22.
//  Copyright © 2020 梁丰. All rights reserved.
//
#define PY_SSIZE_T_CLEAN
//这里导入Python.h的在python安装下的全路径方便开发工具代码提示
#include "/opt/anaconda3/envs/pyenv1/include/python3.7m/Python.h"
#include <stdio.h>
#include <stdlib.h>

//c函数只有两个参数self指向omodule对象
//args就是python传入的参数的包装对象
//此方法相当于python和c的接口和参数适配器
static PyObject *test_system(PyObject *self,PyObject *args){
    char *in_str;
    int in_int;
    //&in_str 是一个二级指针传递的是指针的地址用来给指针在函数里面赋值
    //&in_int 是个一级指针用来给int赋值
    //把z一级指针当作一个类型的话其实就是给该类型变量在函数中赋值的操作
    //PyArg_ParseTuple方法解析python传入的参数
    if(!PyArg_ParseTuple(args,"si",&in_str,&in_int))
        return NULL;
    printf("str:%s,int:%d",in_str,in_int);
    //调用系统命令 当然这里可以调用自己写的c代码
    int rel = system(in_str);
    if(rel < 0){
        return NULL;
    }
    return Py_BuildValue("s","out_str");
}

static PyMethodDef TestMethods[] = {
    //system是python中的函数名，
    //test_system是上面定义的函数，METH_VARARGS表示方法
    {"system",  test_system, METH_VARARGS,
     "Execute a shell command."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef testmodule = {
    PyModuleDef_HEAD_INIT,
    "test4",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    TestMethods
};
PyMODINIT_FUNC
PyInit_test4(void) //PyInit_name name必须是模块名称 而且不能定义为static的 当import此模块时该函数被调用
{
    return PyModule_Create(&testmodule); //创建返回一个module对象 被安装到sys.modules下
}
