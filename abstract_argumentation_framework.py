from itertools import combinations

class AbstractArgumentationFramework:
    """
    Define AbstractArgumentationFramework class using lattice structure
    """
	
    def __init__(self, arguments, attacks):
        """
        Initializes the argumentation framework.
        :param arguments: A set of arguments (e.g., {"A", "B", "C"}).
        :param attacks: A list of attack relations (e.g., [("A", "B"), ("B", "C")]).
        """
        self.arguments = arguments
        self.attacks = {arg: [] for arg in arguments}
        for attacker, attacked in attacks:
            self.attacks[attacker].append(attacked)
    
    def generate_powerset(self):
        """
        Generate the powerset (lattice) of the arguments.
        This is the set of all possible subsets of the arguments.
        """
        subsets = []
        for r in range(len(self.arguments) + 1):
            subsets.extend(combinations(self.arguments, r))
        return [set(subset) for subset in subsets]
    
    def is_conflict_free(self, subset):
        """
        Check if a subset of arguments is conflict-free.
        A subset is conflict-free if no argument in the subset attacks another.
        :param subset: A subset of arguments.
        :return: True if conflict-free, False otherwise.
        """
        for arg in subset:
            if any(attacked in subset for attacked in self.attacks.get(arg, [])):
                return False
        return True
    
    def is_admissible(self, subset):
        """
        Check if a subset of arguments is admissible.
        A subset is admissible if:
          1. It is conflict-free.
          2. Every argument in the subset is defended against attackers.
        :param subset: A subset of arguments.
        :return: True if admissible, False otherwise.
        """
        if not self.is_conflict_free(subset):
            return False

        for arg in subset:
            # Check if argument is defended
            attackers = [attacker for attacker, targets in self.attacks.items() if arg in targets]
            for attacker in attackers:
                # Argument is defensible if there's another argument that blocks the attack
                if not any(defender in subset and attacker in self.attacks.get(defender, []) for defender in subset):
                    return False
        return True
      
    def grounded_extension(self):
        """
        Compute the grounded extension.
        The grounded extension is the minimal admissible set.
        If the minimal set is empty, return the smallest non-empty admissible set.
        :return: The grounded extension as a set of arguments.
        """
        lattice = self.generate_powerset()  # Generate all subsets
        admissible_sets = [subset for subset in lattice if self.is_admissible(subset)]

        # Return the smallest non-empty admissible set
        if admissible_sets:
            non_empty_sets = [s for s in admissible_sets if s]
            if non_empty_sets:
                min_length = min(len(s) for s in non_empty_sets)
                smallest_sets = [s for s in non_empty_sets if len(s) == min_length]
            else:
                smallest_sets = set()
        return smallest_sets