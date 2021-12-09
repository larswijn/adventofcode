import useful_functions

puzzle_input = "59717238168580010599012527510943149347930742822899638247083005855483867484356055489419913512721095561655265107745972739464268846374728393507509840854109803718802780543298141398644955506149914796775885246602123746866223528356493012136152974218720542297275145465188153752865061822191530129420866198952553101979463026278788735726652297857883278524565751999458902550203666358043355816162788135488915722989560163456057551268306318085020948544474108340969874943659788076333934419729831896081431886621996610143785624166789772013707177940150230042563041915624525900826097730790562543352690091653041839771125119162154625459654861922989186784414455453132011498"


def correct_signal(signal, repetition_signal=1, correction_pattern=[0, 1, 0, -1], nr_phases=1, allow_printing=True):
    if type(signal) in {int, str}:
        signal = [int(x) for x in str(signal)]
    if repetition_signal == 1:
        repetition_signal = 0
    original_correction_pattern = useful_functions.deepish_copy(correction_pattern)
    correction_pattern = useful_functions.deepish_copy(correction_pattern)

    for _ in range(nr_phases):
        next_signal = []
        for i in range(len(signal)):
            sub_signal = []
            for index, item in enumerate(signal, start=1):
                if correction_pattern[index % len(correction_pattern)] == 0:
                    continue
                if allow_printing:
                    print(f"  {item} * {correction_pattern[index % len(correction_pattern)]}",
                          end=' = ' if index == len(signal) else ' +')
                sub_signal.append(item * correction_pattern[index % len(correction_pattern)])
            sum_sub_signal = sum(sub_signal)
            if allow_printing:
                print(sum_sub_signal, '->', str(sum_sub_signal)[-1])
            next_signal.append(str(sum_sub_signal)[-1])
            # print(f"  correction pattern:", correction_pattern)

            for index, item in reversed(list(enumerate(original_correction_pattern))):
                correction_pattern.insert((i + 1) * index, item)
        if allow_printing:
            print(''.join(map(str, signal)))
        signal, next_signal = [int(x) for x in ''.join(next_signal)], []
        correction_pattern = useful_functions.deepish_copy(original_correction_pattern)

    return ''.join(map(str, signal))


def predict_end_corrected_signal(signal):
    # FAILS
    # we seem to be able to predict the final 40% of the corrected signal (100 phases); replace unknowns with *
    if type(signal) in {int, str}:
        signal = [int(x) for x in str(signal)]
    length_full_signal = len(signal)
    signal = signal[length_full_signal // 5 * 3:][::-1]
    # corrections are like: '0' x 4, '5' x 4, '0' x 4, '5' x 4, etc  (apply on the reversed end of the signal)
    repeated = 0
    current_diff = 0
    for index, item in enumerate(signal):
        if repeated == 4:
            repeated = 0
            current_diff = 5 if current_diff == 0 else 0
        signal[index] = (item + current_diff) % 10
        repeated += 1
    signal = ''.join(map(str, reversed(signal)))
    signal = '*'*(length_full_signal-len(signal)) + signal
    return signal


def main():
    print("initialized day16")
    pass
