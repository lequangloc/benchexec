"""
BenchExec is a framework for reliable benchmarking.
This file is part of BenchExec.

Copyright (C) 2007-2015  Dirk Beyer
All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import benchexec.util as util
import benchexec.tools.template
import benchexec.result as result

class Tool(benchexec.tools.template.BaseTool):
    """
    Tool wrapper for Forest
    """
    def executable(self):
        return util.find_executable('forest')

    def name(self):
        return 'Forest'

    def version(self, executable):
        return self._version_from_tool(executable)

    def cmdline(self, executable, options, tasks, propertyfile, rlimits):
        assert len(tasks) == 1, "only one inputfile supported"
        return [executable] + ["-propertyfile", propertyfile] + options + ["-svcomp_only_output"] + [ tasks[0] ]

    def determine_result(self, returncode, returnsignal, output, isTimeout):
        status = result.RESULT_UNKNOWN
        if "TRUE" in output:
            status = result.RESULT_TRUE_PROP
        if "FALSE_REACH" in output:
            status = result.RESULT_FALSE_REACH
        if "FALSE_DEREF" in output:
            status = result.RESULT_FALSE_DEREF
        if "FALSE_FREE" in output:
            status = result.RESULT_FALSE_FREE

        return status
