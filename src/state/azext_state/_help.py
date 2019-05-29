# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

helps['state'] = """
    type: group
    short-summary: Faster, tenant wide governance summarizing.
"""

helps['state resources'] = """
    type: command
    short-summary: Support for tenant-wide hiearchy querying.
    examples:
        - name: Capture the tenant-wide existing resource hierarchy.
          text: >
            az state resources --scope tenant                  
"""

helps['state role-definitions'] = """
    type: command
    short-summary:
    examples:
        - name:
          text: >
            az state        
"""

helps['state role-assignments'] = """
    type: command
    short-summary:
    examples:
        - name:
          text: >
            az state 
"""

helps['state policy-definitions'] = """
    type: command
    short-summary:
    examples:
        - name:
          text: >
            az state 
"""

helps['state policy-assignments'] = """
    type: command
    short-summary:
    examples:
        - name:
          text: >
            az state 
"""

helps['state locks'] = """
    type: command
    short-summary:
    examples:
        - name:
          text: >
            az state 
"""