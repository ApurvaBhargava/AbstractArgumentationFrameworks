from itertools import combinations

class FuzzyArgumentationFramework:
    """
    Define class for fuzzy argumentation using lattice structure
    and argument probabilities
    """
	
    def __init__(self, arguments, attacks, probabilities, conflict_threshold):
        """
        Initializes the fuzzy argumentation framework.
        :param arguments: A set of arguments (e.g., {"A", "B", "C"}).
        :param attacks: A list of attack relations (e.g., [("A", "B"), ("B", "C")]).
        :param probabilities: A dictionary with argument probabilities 
                               (e.g., {"A": 0.9, "B": 0.8, "C": 0.6}).
        """
        self.arguments = arguments
        self.attacks = {arg: [] for arg in arguments}
        for attacker, attacked in attacks:
            self.attacks[attacker].append(attacked)
        self.probabilities = probabilities  # Argument probabilities (0 <= p <= 1)
        self.conflict_threshold = conflict_threshold
    
    def generate_powerset(self):
        """
        Generate the powerset (lattice) of the arguments, along with their joint probabilities.
        This is the set of all possible subsets of the arguments, with each subset paired with 
        the product of the probabilities of the arguments in that subset.
        """
        subsets_with_probs = []
        for r in range(len(self.arguments) + 1):
            for subset in combinations(self.arguments, r):
                joint_probability = 1.0
                for arg in subset:
                    joint_probability *= self.probabilities.get(arg, 0)  # Multiplies probability of each argument in the subset
                subsets_with_probs.append((set(subset), joint_probability))
        return subsets_with_probs
    
    def is_conflict_free(self, subset):
        """
        Check if a subset of arguments is conflict-free considering their probabilities.
        A conflict is significant if the product of the attacking arguments' probabilities 
        exceeds the conflict threshold.
        """
        for arg in subset:
            for attacked in self.attacks.get(arg, []):
                if attacked in subset:
                    # Calculate the combined probability of the conflict
                    conflict_prob = self.probabilities.get(arg, 0) * self.probabilities.get(attacked, 0)
                    if conflict_prob > self.conflict_threshold:
                        return False
        return True
    
    def is_admissible(self, subset):
        """
        Check if a subset of arguments is admissible.
        """
        if not self.is_conflict_free(subset):
            return False

        for arg in subset:
            # Get all attackers for the argument
            attackers = [attacker for attacker, targets in self.attacks.items() if arg in targets]
            for attacker in attackers:
                # Find defenders in the subset
                defenders = [
                    defender for defender in subset if attacker in self.attacks.get(defender, [])
                ]
                # Check if there's no defender or if the strongest defender is weaker than the attacker
                if not defenders or self.probabilities.get(attacker, 0) > max(self.probabilities.get(defender, 0) for defender in defenders):
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
        admissible_sets = [subset[0] for subset in lattice if self.is_admissible(subset[0])]

        # Filter non-empty admissible sets and find the smallest one
        non_empty_sets = [s for s in admissible_sets if s]
        if non_empty_sets:
            min_length = min(len(s) for s in non_empty_sets)
            smallest_sets = [s for s in non_empty_sets if len(s) == min_length]
            return smallest_sets
        return []  # Return empty list if no admissible sets found
