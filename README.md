# BenchExec
## A Framework for Reliable Benchmarking and Resource Measurement

[![Build Status](https://travis-ci.org/dbeyer/benchexec.svg?branch=master)](https://travis-ci.org/dbeyer/benchexec)
[![Code Quality](https://api.codacy.com/project/badge/grade/d9926a7a5cb04bcaa8d43caae38a9c36)](https://www.codacy.com/app/PhilippWendler/benchexec)
[![Test Coverage](https://api.codacy.com/project/badge/coverage/d9926a7a5cb04bcaa8d43caae38a9c36)](https://www.codacy.com/app/PhilippWendler/benchexec)
[![PyPI version](https://badge.fury.io/py/benchexec.svg)](https://badge.fury.io/py/benchexec)
[![Apache 2.0 License](https://img.shields.io/badge/license-Apache--2-brightgreen.svg?style=flat)](http://www.apache.org/licenses/LICENSE-2.0)
    
**News**: We have published a paper titled
[Benchmarking and Resource Measurement](http://www.sosy-lab.org/~dbeyer/Publications/2015-SPIN.Benchmarking_and_Resource_Measurement.pdf)
on BenchExec and its background
at [SPIN 2015](http://www.spin2015.org/).
It also contains a list of rules that you should always follow when doing benchmarking
(and which BenchExec handles for you).

BenchExec provides three major features:

- execution of arbitrary commands with precise and reliable measurement
  and limitation of resource usage (e.g., CPU time and memory)
- an easy way to define benchmarks with specific tool configurations
  and resource limits,
  and automatically executing them on large sets of input files
- generation of interactive tables and plots for the results

Contrary to other benchmarking frameworks,
it is able to reliably measure and limit resource usage
of the benchmarked tool even if it spawns subprocesses.
In order to achieve this,
it uses the [cgroups feature](https://www.kernel.org/doc/Documentation/cgroups/cgroups.txt)
of the Linux kernel to correctly handle groups of processes.
BenchExec is intended for benchmarking non-interactive tools on Linux systems.
It measures CPU time, wall time, and memory usage of a tool,
and allows to specify limits for these resources.
It also allows to limit the CPU cores and (on NUMA systems) memory regions.
In addition to measuring resource usage,
BenchExec can verify that the result of the tool was as expected,
and extract further statistical data from the output.
Results from multiple runs can be combined into CSV and interactive HTML tables,
of which the latter provide scatter and quantile plots.

BenchExec was originally developed for use with the software verification framework
[CPAchecker](http://cpachecker.sosy-lab.org)
and is now developed as an independent project
at the [Software Systems Lab](http://www.sosy-lab.org) at the [University of Passau](http://www.uni-passau.de).

### Links

- [Documentation](https://github.com/dbeyer/benchexec/tree/master/doc/INDEX.md)
- [Downloads](https://github.com/dbeyer/benchexec/releases)
- [Changelog](https://github.com/dbeyer/benchexec/tree/master/CHANGELOG.md)
- [BenchExec GitHub Repository](https://github.com/dbeyer/benchexec),
  use this for [reporting issues and asking questions](https://github.com/dbeyer/benchexec/issues)
- [BenchExec at PyPI](https://pypi.python.org/pypi/BenchExec)
- Paper [Benchmarking and Resource Measurement](http://www.sosy-lab.org/~dbeyer/Publications/2015-SPIN.Benchmarking_and_Resource_Measurement.pdf) about BenchExec ([supplementary webpage](http://www.sosy-lab.org/~dbeyer/benchmarking/))

### Users of BenchExec

BenchExec was successfully used for benchmarking in all four instances
of the [International Competition on Software Verification](http://sv-comp.sosy-lab.org)
with a wide variety of benchmarked tools and hundreds of thousands benchmark runs.

The developers of the following tools use BenchExec:

- [CPAchecker](http://cpachecker.sosy-lab.org), also for regression testing
- [SMACK](https://github.com/smackers/smack)

If you would like to be listed here, [contact us](https://github.com/dbeyer/benchexec/issues/new).
