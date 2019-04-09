#!/usr/bin/env bash

mkdir -p days/day${1}
mkdir -p tests/day${1}


PUZZLE=days/day${1}/puzzle_${1}.py
if [[ ! -e ${PUZZLE} ]]; then
    echo "def solve_${1}():" > ${PUZZLE}
    echo "    pass" >> ${PUZZLE}
    echo "" >> ${PUZZLE}
    echo "" >> ${PUZZLE}
    echo "if __name__ == '__main__':" >> ${PUZZLE}
    echo "    r = solve_${1}()" >> ${PUZZLE}
    git add ${PUZZLE}
fi

TEST=tests/day${1}/test_${1}.py
if [[ ! -e ${TEST} ]]; then
    touch `dirname ${TEST}`/__init__.py
    echo "from unittest import TestCase" > ${TEST}
    echo "" >> ${TEST}
    echo "from days.day${1}.puzzle_${1} import solve_${1}" >> ${TEST}
    echo "" >> ${TEST}
    echo "" >> ${TEST}
    echo "class TestSolve${1}(TestCase):" >> ${TEST}
    echo "    pass" >> ${TEST}
    git add ${TEST}
    git add `dirname ${TEST}`/__init__.py
fi



