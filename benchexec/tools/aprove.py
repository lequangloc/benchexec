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

    REQUIRED_PATHS = [
                  "aprove.jar",
                  "AProVE.sh",
                  "bin",
                  "newstrategy.strategy"
                  ]

    def executable(self):
        return util.find_executable('AProVE.sh')


    def name(self):
        return 'AProVE'


    def determine_result(self, returncode, returnsignal, output, isTimeout):
        output = '\n'.join(output)
        if "YES" in output:
            return result.RESULT_TRUE_PROP
        elif "TRUE" in output:
            return result.RESULT_TRUE_PROP
        elif "FALSE" in output:
            return result.RESULT_FALSE_TERMINATION
        elif "NO" in output:
            return result.RESULT_FALSE_TERMINATION
        else:
            return result.RESULT_UNKNOWN
