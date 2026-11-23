import itertools
import json


def coefficients(radix, bound, limit):
    counts = [0] * (limit + 1)
    counts[0] = 1
    weight = 1
    while weight <= limit:
        previous = counts
        counts = [0] * (limit + 1)
        for residue in range(weight):
            subtotal = 0
            for number in range(residue, limit + 1, weight):
                subtotal += previous[number]
                expired = number - (bound + 1) * weight
                if expired >= 0:
                    subtotal -= previous[expired]
                counts[number] = subtotal
        weight *= radix
    return counts


def recurrence(radix, bound, limit):
    counts = [1] + [0] * limit
    for number in range(1, limit + 1):
        counts[number] = sum(
            counts[(number - digit) // radix]
            for digit in range(number % radix, min(bound, number) + 1, radix)
        )
    return counts


def logarithm_floor(number, radix):
    exponent = 0
    power = radix
    while power <= number:
        exponent += 1
        power *= radix
    return exponent


def two_digit_choices(number, radix, quotient_choices):
    remainder = number % radix
    top = min(quotient_choices - 1 - (remainder == radix - 1), number // radix)
    total = 0
    for quotient in range(top + 1):
        residual = number // radix - quotient
        next_top = min(
            quotient_choices - 1 - (residual % radix == radix - 1),
            residual // radix,
        )
        total += next_top + 1
    return total


def run():
    limit = 5000
    comparisons = 0
    quotient_bounds = 0
    threshold_bounds = 0
    plateau_counts = 0
    unique_counts = 0
    endpoint_identities = 0
    critical_counts = 0
    carry_constructions = 0
    pair_bounds = 0
    higher_threshold_bounds = 0
    for radix in range(2, 11):
        for bound in range(radix - 1, radix**2):
            counts = coefficients(radix, bound, limit)
            assert counts == recurrence(radix, bound, limit)
            comparisons += limit + 1
            choices = bound // radix + 1
            for number in range(1, limit + 1):
                exponent = logarithm_floor(number, radix)
                assert 1 <= counts[number] <= choices**exponent
                quotient_bounds += 1
                if bound < radix**2 - 1:
                    assert counts[number] <= radix**(exponent % 2) * (radix**2 - 1)**(exponent // 2)
                    threshold_bounds += 1
                else:
                    assert counts[number] == number // radix + 1
                    critical_counts += 1
            for choices in range(2, radix + 1):
                if not (choices - 1) * (radix + 1) <= bound <= choices * radix - 1:
                    continue
                repunit = 1
                exponent = 0
                while (choices - 1) * repunit <= limit:
                    assert counts[(choices - 1) * repunit] == choices**exponent
                    plateau_counts += 1
                    repunit = repunit * radix + 1
                    exponent += 1
            if bound <= 2 * radix - 2:
                power = radix
                while power - 1 <= limit:
                    assert counts[power - 1] == 1
                    unique_counts += 1
                    power *= radix
        for multiplier in range(1, radix + 4):
            counts = coefficients(radix, multiplier * radix - 1, limit)
            quotient = coefficients(radix, multiplier - 1, limit // radix)
            cumulative = list(itertools.accumulate(quotient))
            for number, count in enumerate(counts):
                assert count == cumulative[number // radix]
                endpoint_identities += 1
        for choices in range(2, radix + 1):
            for exponent in range(7):
                if choices**exponent > 4096:
                    break
                images = set()
                target = (choices - 1) * sum(radix**index for index in range(exponent + 1))
                for interior in itertools.product(range(choices), repeat=exponent):
                    carries = (0,) + interior + (0,)
                    digits = tuple(
                        choices - 1 + radix * carries[index + 1] - carries[index]
                        for index in range(exponent + 1)
                    )
                    assert all(0 <= digit <= (choices - 1) * (radix + 1) for digit in digits)
                    assert sum(digit * radix**index for index, digit in enumerate(digits)) == target
                    assert digits not in images
                    images.add(digits)
                    carry_constructions += 1
                assert len(images) == choices**exponent
        for threshold_power in range(2, 5):
            choices = radix**(threshold_power - 1)
            gap = choices**2 - choices // radix
            start = radix * (radix + 2) * choices
            largest = 0
            for number in itertools.chain(range(101), range(start, start + radix**2)):
                pairs = two_digit_choices(number, radix, choices)
                assert pairs <= gap
                largest = max(largest, pairs)
                pair_bounds += 1
            assert largest == gap
            if threshold_power > 2:
                counts = coefficients(radix, radix**threshold_power - 2, 2000)
                assert counts == recurrence(radix, radix**threshold_power - 2, 2000)
                comparisons += 2001
                for number in range(1, 2001):
                    exponent = logarithm_floor(number, radix)
                    assert counts[number] <= choices**(exponent % 2) * gap**(exponent // 2)
                    higher_threshold_bounds += 1
    five = coefficients(4, 5, 6)[6]
    six = coefficients(4, 6, 6)[6]
    assert (five, six) == (1, 2)
    return {
        'status': 'pass',
        'arithmetic': 'exact integers',
        'radices': {'minimum': 2, 'maximum': 10},
        'coefficient_range': {'minimum': 0, 'maximum': limit},
        'digit_bounds': 'radix-1 through radix^2-1; additional endpoint multipliers 1 through radix+3',
        'coefficient_comparisons': comparisons,
        'quotient_upper_bound_cases': quotient_bounds,
        'linear_threshold_upper_bound_cases': threshold_bounds,
        'plateau_repunit_count_cases': plateau_counts,
        'unique_all_maximum_digit_cases': unique_counts,
        'summatory_identity_cases': endpoint_identities,
        'critical_linear_identity_cases': critical_counts,
        'carry_parameters': '2<=q<=radix, 0<=m<=6, q^m<=4096',
        'distinct_carry_constructions': carry_constructions,
        'two_digit_branching_cases': pair_bounds,
        'higher_threshold_parameters': 'r=3,4; k=radix^r-2; 1<=n<=2000',
        'higher_threshold_upper_bound_cases': higher_threshold_bounds,
        'printed_exponent_counterexample': {'radix': 2, 'digit_bound': 3, 'exact_count': 'floor(n/2)+1', 'logarithmic_exponent': 1},
        'strict_point_count_example': {'radix': 4, 'number': 6, 'bound_5_count': five, 'bound_6_count': six},
        'scope': 'Finite coefficient identities, carry constructions, and branching bounds; all limiting and threshold statements have written proofs in note.tex.',
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
