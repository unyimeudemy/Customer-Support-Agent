from main.lib.function_registry import FUNCTION_REGISTRY


def workflow_executor(workflow, user_id):
    context = {}
    context["phone"] = user_id

    for step in workflow["steps"]:
        if "action" in step:
            action_name = step["action"]
            func = FUNCTION_REGISTRY[action_name]
            context = func(context)

        elif "decision" in step:
            decision_name = step["decision"]
            condition = decision_name[0]["if"]
            condition_value = context.get(condition)
            
            if condition_value:
                branch = decision_name[0]["then"]
            else:
                branch = decision_name[1]["else"]
                if isinstance(branch, dict):
                    branch = [branch]
        
            for action in branch:
                action_name = action["action"]
                func = FUNCTION_REGISTRY[action_name]
                context = func(context)

    return context