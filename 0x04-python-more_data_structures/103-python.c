#include <Python.h>
#include <stdio.h>

/* Function to print basic info about Python lists */
void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid Python list object.\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    PyObject *repr = PyObject_Repr(p);
    const char *list_repr = PyUnicode_AsUTF8(repr);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
    printf("[*] %s\n", list_repr);
    Py_XDECREF(repr);
}

/* Function to print basic info about Python bytes objects */
void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid Python bytes object.\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    const char *bytes_data = PyBytes_AsString(p);
    printf("[.] bytes object info\n");
    printf("  [.] size: %zd\n", size);
    printf("  [.] trying string: %s\n", bytes_data);
    printf("  [.] first 10 bytes: ");
    for (Py_ssize_t i = 0; i < size && i < 10; ++i) {
        printf("%02x ", (unsigned char) bytes_data[i]);
    }
    printf("\n");
}