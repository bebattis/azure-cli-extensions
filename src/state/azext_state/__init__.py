# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

import azext_state._help  # pylint: disable=unused-import


class StateCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        state_custom = CliCommandType(
            operations_tmpl='azext_state.custom#{}')
        super(StateCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                      custom_command_type=state_custom)

    def load_command_table(self, _):
        with self.command_group('state') as g:
            g.custom_command('resources', 'state_resources')
            g.custom_command('role-definitions', 'state_role_definitions')
            g.custom_command('role-assignments', 'state_role_assignments')
            g.custom_command('policy-definitions', 'state_policy_definitions')
            g.custom_command('policy-assignments', 'state_policy_assignments')
            g.custom_command('locks', 'state_locks')
        return self.command_table

    def load_arguments(self, _):
        with self.argument_context('state resources') as c:
            c.argument('')
            
        with self.argument_context('state role-definitions') as c:

        with self.argument_context('state role-assignments') as c:

        with self.argument_context('state policy-definitions') as c:

        with self.argument_context('state policy-assignments') as c:

        with self.argument_context('state locks') as c:


COMMAND_LOADER_CLS = StateCommandsLoader
