#!/usr/bin/python3
"""
This module multiply two matricies using numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply two matrix that is given
    Args:
        m_a: the input first matrix
        m_b: the input second matrix
    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
