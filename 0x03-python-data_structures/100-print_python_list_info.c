#include <Python.h>

/**
 * print_python_list_info - prints info of a Python object.
 * @p: Python object.
 */

void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *element;

	printf("[*] Size of the Python List = %d\n", ((int)Py_SIZE(p)));
	printf("[*] Allocated = %d\n", ((int)((PyListObject *)p)->allocated));
	for (i = 0; i < Py_SIZE(p); i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
