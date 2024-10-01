#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>

/**
 * print_python_float - prints info about python float
 * @p: address of the pyobject struct
 */
void print_python_float(PyObject *p)
{
    double dble;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
    dble = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %s\n",
        PyOS_double_to_string(dble, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}

/**
 * print_python_bytes - prints info about python bytes
 * @p: address of the pyobject struct
 */
void print_python_bytes(PyObject *p)
{
	size_t k, leng, size;
	char *string;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;
	leng =  size + 1 > 10 ? 10 : size + 1;
	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %lu bytes: ", leng);
	for (k = 0; k < leng; k++)
		printf("%02hhx%s", string[k], k + 1 < leng ? " " : "");
	printf("\n");
}

/**
 * print_python_list - prints info about python lists
 * @p: address of the pyobject struct
 */
void print_python_list(PyObject *p)
{
	int k;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %lu\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (k = 0; k < ((PyVarObject *)p)->ob_size; k++)
	{
		printf("Element %d: %s\n", k,
			((PyListObject *)p)->ob_item[k]->ob_type->tp_name);
		if (!strcmp(((PyListObject *)p)->ob_item[k]->ob_type->tp_name, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[k]);
		else if (!strcmp(((PyListObject *)p)->ob_item[k]->ob_type->tp_name, "float"))
			print_python_float(((PyListObject *)p)->ob_item[k]);

	}
}
