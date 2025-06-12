from main.lib.function_registry import FUNCTION_REGISTRY




class WorkflowExecutor:
    def __init__(self, workflow, user_id):
        self.workflow = workflow
        self.context = {"phone": user_id}

    def execute(self):
        for step in self.workflow.get("steps", []):
            self._process_step(step)
        return self.context

    def _process_step(self, step):
        if "action" in step:
            self._process_action(step["action"])
        elif "decision" in step:
            self._process_decision(step["decision"])
        else:
            raise ValueError(f"Unknown step type: {step}")

    def _process_action(self, action_name):
        func = FUNCTION_REGISTRY.get(action_name)
        if not func:
            raise ValueError(f"Action '{action_name}' not found in function registry.")
        self.context = func(self.context)

    def _process_decision(self, decision_branch):
        condition_key = decision_branch[0]["if"]
        condition_value = self.context.get(condition_key)

        if condition_value:
            branch = decision_branch[0]["then"]
        else:
            branch = decision_branch[1]["else"]

        for action in branch:
            self._process_action(action["action"])
