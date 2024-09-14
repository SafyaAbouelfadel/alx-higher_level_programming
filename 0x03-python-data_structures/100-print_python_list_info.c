#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, allocate, k;
	PyObject *obj;

	size = Py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (k = 0; k < size; k++)
	{
		printf("Element %d: ", k);

		obj = PyList_GetItem(p, k);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
