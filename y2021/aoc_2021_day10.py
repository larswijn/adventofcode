from __future__ import annotations

import statistics

puzzle_input = '{<{<[{<[<([[(<<>[]>[<>()]){(()<>){<>{}}}]<{<{}<>){()<>}}[[()[]]{(){}}]>]{<([[]][{}<>]){<{}<>>{[]<>}}><[(\n[<{(([{<[(<{[{()()}{()[]}]{[<>[]]}}>)[[{[<[][]>(()[])]<({}<>)<()<>>>}([({}{}){[]<>}])]<{{([][])[()\n([<[{[{[{(<{<[[]][[][]]>[(<>[])<[]()>]]<({()<>}([]<>))>>)((([[{}{}]](<(){}><[]{}>))<<{{}[]}[<>()]><[[][]](()(\n(<<<{{{[[<(((<[]()><{}{}>)([<>{}](<>{}}))([(()())[[]<>]]<{[]()}(<>[])>))[[[<{}[]>({}{})]]<{[<>()]((){})}<<[][\n{{[<{([[[([(<(<><>)>{([][]){()[]}})<{{{}()}<()<>>}>])]]<({<{(<()<>>([][]))<<(){}>]}{{<()()\n<[{({[(<[<{{<(<>[])<[][]>]}}((((()<>)<<>[]>)[[<>{}]<{}>]){{(()[])}})>(<<(([]{})<<>[]>)[([][])\n((<[[(([{[[{((()())[{}{}])([(){}]<{}[]>)][[{{}{}}[[][]]][(()())(<>[])]]]{<[[{}[]]]<<()<>>[\n([(<<(<<[[<{{([]())[()<>]}<{<><>}[<>[]]>}{<<[][]>[[][]]><[[]<>}({}<>)>}>[[<([]{})>{({}{})[()[]]}][<{[]\n<<[[<{[<<[<<[{<>[]}({}[])]<[[][]]<{}()>>>((<{}[]>{{}{}}>(<<>{}>([]{})))>(<(<[]()>(<>{}))<((){\n<{<[[<([[[[[<[{}{}](<><>)><{()<>}[{}()]>]{<<()()>{{}{}}>[[()<>][{}()]]}]{{({[]()}[[]<>])(<<>{}>\n([{[[<(({<((({()()}({}{}))<<{}()><[]<>>>)([{{}<>}][<[][]>(<><>)]))>{{[[[{}[]]([]<>)][{()<>}]][([[]{}]{<>[]})]\n(<(<{<{{({<({[{}[]]<(){}>}[<<>[])(<>{})])[[<{}<>>[[]<>]][([]{})<<>[]>]]>[{([{}<>]([]<>))<[<>()\n(({[[[<{([[{<[{}()]<[]<>>>}]{<[<{}>{<><>}]>{{(()[])}<[<>{}]{<>[]})}}]{[[<[<>]{{}[]}><[()[]]{{}\n{[[{{<({{<<<{[<>()]{{}()}}[([]<>){()<>}]>>(<{(<><>){[][]}}[{[]{}}([][])]>{[{()[]}{<>}}{{{}{}}<\n(<<[{[[{<<{{{<[]()>}}<[{()()}(<><>)](<(){}>[{}[]])>}<{{[()[]]([]{})}}{{((){}){[]()}}[({}{})<\n<<<{<{{([<<{[{<><>}((){})]{(<><>)(()<>)})<{[{}<>]{<>()}}{<()[]><(){}>}>>>{{<<<[]()>{()[]}>({\n{[(<[[{[(({<(<{}<>>{<>()}>({[]{}})>[[(()<>){<>[]}][[<><>]{<>{}}]]}))[[{{[<()[]>(()<>)]}}([([<>{\n<([({((<((({[<()<>>]<<()[]>(()[])>}{({()[]}[[]{}])})<[{[()<>](<>{})}<(<>{}){()[]}>]<((()())[[]()])>>))><\n{{([([(<((([[({}[])(<>{})][<()()>{<>()}]])[{{[()<>]{{}()}}<[()()][()[]]>}]){{{[{[]()}]}<[<<>(\n<[[{((<{{{(<((<>{})[{}[]])(<()[]><()()>)>{[{<>()}[()[]]]{{[]<>}<<><>>}})}(<{<(<>)[()]>}>)}<{<[([<>{}][(){}])\n<{[<[{[<{[(<[[<>[]]<{}<>>]>[[<<>[]>{{}[]}]{({}[])[[]<>]}])]{{{<<{}{}>{<>()}>[{()<>}{(){}}]}{<[()()][(){}]\n({<([<[<((<({({}[])<[][]>})[<[<>()]([]{})><(<><>){{}[]}>]>))[<[<([[][]]{{}[]})>](<(<<>()>)(<{}<>>)>)>]>]>]\n{{{[{{<<{<[<(<<>[]>[{}{}])>[[{{}<>}<<>[]>][[[]<>]<[]{}>]]]{<({()<>}((){})){[[][]]<[]>}>[<(<>[])>([{\n{<({[{{{(<{<[<[]<>>]{{{}[]}<<><>>}>{[[<>[]]<{}[]>]}}(<(<()()><{}[]>)>{[[()()][()<>]]})><(({[()()]}[[[\n<<[{<{{<(<({[<()()>{()<>}]((()[]){[]{}})}{[(()[])[{}{})]{({}<>){<>()}}}){({<{}<>>[{}]}(<{}[]>))[{[[]\n<[((<[{<<<(({[[]{}](<>)}{({}{})})(({{}{}})<{()()}>})<<([()[]]{<>()}){([]()){<><>}}>>>>{(<<{<{}()>{()<>}}(\n{(({[[<{[{[(({{}<>}(()[]))[([]{}){()()}])](<<{{}()}{<>{}}><<{}[]><{}()>>><[[<>()][()]]({<>\n[[({<(<[[({[{<{}[]>(()<>)}<{()()}>][[[{}<>](()[])]{(<><>){()<>}}]}[([{<><>}<<>()>]<{{}()}<<>{}>>)[{{(\n[[<(([<{{{<{({<>{}}{<>{}})}<[<{}[]>(<>[])]<((){})>>>{[{<{}[]>{{}[]}}{<[][]>{{}<>}}]{(<[][]>{()))<<[]{}>{(\n(<[{<<({<<{{(([]()){[]()})[({}{})]}({({}{})<{}{}>}(({}){{}<>}))}{<<<{}{}><{}()>><[{}()][[]]>>}>>[<{({({})[<>\n{([(<([[<{(<({()[]>[<><>]){[[]<>](<><>)}>{{[()<>]({}{})}<{<>[]}[(){}]>})}{(({<[]()>{{}()}}{{<>()}(<\n(<<[{([<[{{[[([]{})]<(()<>){<><>}>]<[{<>[]}<{}[]>]>}<<{([]<>)[{}<>]}(([]<>)<<>()>)>[<{<>{}}\n<[([[<<<<<({<[()[]]>}[<({}<>)>])[[({{}()}(()<>))<<<><>>{[]{}}>]{{[<>()][[][]]}{<{}{}>({}())}}]>[{{{[\n[<{[(<[<<{<(<{<>()}>[{{}()}{{}{}}])>}>([<[<[[][]]>((()<>)<(){}>)]{(<()>)(<<>[]>({}()))}>([[<[]<>>\n<[(([<{(<<<{{<[]<>><[]<>>}{<()[]>(<>())}}<{<<>()>{[]}}(<()<>>[[]{}])>>>[<{([()[]]<{}()>)<<{}{}>{{}[]}>}{((<\n[{<[{[([(<({<<<>{}><<><>>>{(()()){()[]}}}({[<>[]]<<><>>}([()]({}<>)))){{{[[]{}]{{}<>}}[(<>{}){<>}]}[<{[][]}\n<<<{({[(({[{({<><>}([][])){{<><>}[(){}]}}(([{}{}][{}[]]))]({<({}<>){{}()}>[[{}[]]{[]{}}]}}}))]<[[<(<{{()\n[(([[(<({{({(<()()>(<>{}))}({<[]<>>{[]<>}}<[<><>]{[]<>}>)]<([[[]{}][[]{}]]{([][]){()<>}}){{[{}\n<{(<[<{<{([{([()[]]<(){}>)([[]<>]({}()))}](<([[]<>]<<>{}>)[{[]{}}[<><>]]>))}>}>[{<({<<[(()()\n[{({[({<[((({[<>()]<[][]>}{{<>}{(){}}})([(()<>)<<><>>][({}{})<<>[]]]))<<<{{}()}<[]<>>>(<()[]><[]()>)>\n[[<{((<<(<<{(<<>[]>[(){}])(([]<>)([]{}))}<[[(){}]<[]<>>]{(<>())(<>)}>>>)>[{<[{{[<>{}]{[]()}}[\n<([{{{<([([([<(){}><()[]>])([[{}<>]]{[()<>>({}())})]<[<{()[]}{()()}><[[]()][<><>]>]>)]<{({((()()\n<<{([<[[{<[<(({}<>)(()()))({{}[]>[<>()])>{[<{}>]<[{}{}]>}]([{{[]{}}[{}()]}{[()<>]{<>}}]{([<>{}][[]()\n({[[[[(<<{{[{(<>[])[{}]}[<[]<>>[<><>]]]}}([<([<><>]{<>{}})[<[]{}>[<><>]]>{(<()<>>[{}])[([][])[{}{}]]}])>>(\n<({<(<<[({[{{{{}[]}<<><>>}[([][])(()<>)]}]<<[[{}]{<>()}]>>}<<<{<<>[]>([]())}<({}())[<><>]>>{<{<>{}\n(<({{<{[{[({[{[]<>}{()[]}]}<{{{}()}{[]<>}}<<{}<>>[{}{}]>>)[[({{}<>}[<>()])<[{}[]][()()]>]}][{{<[[]{}][[]()]\n(<<[((<{<<{[[{<>{}}[<><>]]{{{}{}}{<>[]}}]<[{()()}([]())](({}()){()[]})>}>)<((<<[{}[]]>[{<>[]}([]{})]>)({({[]<\n([({<<(({((<{[{}[]]<()<>>}{[{}<>][{}()]}>)<<(<{}[]>[[][]]){<()<>)<<>()>}><(<<><>><[]{}>)[<<>()>[<\n[([<[[(((((({<(){}>[{}{}]}([[]()]{()[]})))<[(({}<>)[<>{}])(([][])([]{}))](<[()()]{<>()}><[()[]]{()(\n({[({[{<<({<[(<>())<{}<>>]>[[(<><>)][{{}{}}[{}()]]]}<[([[]<>]([]<>))<[()<>]<()()>>]<{<{}[]>({}())}{<<\n(<<{(<<({{<<<<(){}>([]())>{[()()][{}{}]}>[([[]<>]{{}}){{{}{}}}]>}}{(({{(<><>){<>()}}}[({[]()})[[[]]{[]{}}]]\n((<[([((<[([{[<>()][()()]}{[{}<>][<>[]]}]<(([][])({}())){<()[]>([]())}>)[{{<<><>>([]{}}}[{<><>}<{}[]\n<{(<<[<<<{[{<<[]()>[()<>]>(([]{})([]<>))]{<([][])<<>{}>>{(<>()){()}}}](<{[<>[]]}([()()]{<>{}})>(<[()[]][\n[<{{[[[<[[{((([]())<{}[]>){(<><>)})[{{{}}}[({}[])({}{})]}}{{(([]<>)<<><>>)<([][])({}<>)>}{<<()[]><()()>>[<{}\n<<([(<<({<<(<(<>[]){()[]}>{[()<>)(<><>)})>{((<{}[]>(()[]))({[]<>}[{}{}]))<{<<><>>(<>())}<({}<>)[[]]\n<(<<{[<<[[[{<[<>{}]{<><>}>[<<>[]>[(){}]}}{{<{}{}>}(<<>()><[]()>)}]]{{([[[]{}][[]()]][[<>()][{}[]]]\n(<{<<{<{[{<{<[()()]<{}()]>{<<>()>({})}}>{[{<{}<>>}<<[]<>><[][]>>]<([{}{}][[]<>]){{[][]}{<>}}>}}]\n{{[[([<[[{<[[<[]()>[()<>]]<({}[])[{}[]]>]>}<[((([][]){[]}){<{}{}>((){})})][([([][])({}[])](<{}<>><<>{}>))]>\n[[{{({{[[[{<[{(){}}{[]<>}>[<{}[]>]>}]((<{<(){}><{}()>}[<<><>>({}{})]><<{{}{}}>(({}[]){()<>}\n[<<([<<({[<({{()()}[[]()]}({{}<>}[<>()]))>([[[{}<>]([][])][({}()){[]()}]])]((([[(){}](()<>)](({}{}>))\n<[{<{(<<([({[({}<>)[[][]]]{{[][]}<{}{}>}})([[[[]{}](<>{})]([<><>](()()))]{{([])[()()]}({<>[]})])]<<(({[](\n[((<<[<[{<[{{[()[]]({}())}([[]{}]<()[]>)}[(<[]()>{()[]})<<<>()>[()()]>}]({{[{}{}][()[]]}{{<>()}\n{{{{<[([([<({{[]()}<(){}>}{(()[])<<>()>})>{([({}[])<[]<>>][[[]()]])}]<{<((<>)[()<>])<(()<>)\n[[<{<([[([<[{[<><>]{(){}}}{(<>()){{}}}]>[[{{<>[]}{[]}}]]][<{[<{}()>]<[{}()][<><>]>}(<{[]<>\n((<[<{<<<{<<{[[]{}]}>{<(<><>)<<>()>>{(<><>)({}())})>{{<([]{})<[]()>>{[<>{}][()()]}}[<<<>{}>([]{})>[{{}}<()()\n<<({(<{[[<((<{<>[]}(()())>>[<[[]<>][<>{}]>])[(<{{}{}}><<<>()>>)(([[]()]{[]<>}))]><<[{<[]{}><()[\n(({({({<(([[{({}[])([]())}]({<<>{}>[()<>]}{<[][]>({}[])})][{{[[]<>]}}{[<<>><{}{}]]}])<<[{{()[]}\n<[(([<(<{[[([((){}){{}<>}]<[{}{}]{()<>}>)<<{<>[]}[(){}]><({}())([][])>>]<[{<()()>{<><>}}[(<>{}]([]())]][{\n{[<{([{<[{<[<<{}<>>[{}{}]>[[<><>](<>[])]]<{<(){}>([]<>)}{{()<>}([]())}>>{(<(<>)[()<>]>{[{}[]]\n{(((((<<[[{(([(){}]<[]()>)[<<><>>])<<{()}{<>[]}><(<>[]){{}{}}>>}({<[{}<>]([]<>)>{{{}{}}<<>{}>}}{([\n<{{<<<(<{{<([<()()>([]<>)]<{()()}<()<>>>){<<[]{}><[][]>><{{}<>}>}>{([[<>]{[]()}][<{}><[][]>])[{((){})<\n{{[{[{([{<{<[{()()}{()}]([<>{}][{}{}])><<[[]()]>({()<>}<[][]>)>}({((<>())({}()))[[{}()][<>[]]]}<{([]<>)<{}<\n{([<[<(<[([<[{<><>}[{}{}]](<{}<>>[[]<>])>[{{[][]}[{}()]}(<{}[]><{}{}>)]])]<<<[<(<><>)<<>>>{[{}()]}]<\n<<[(([[{{({(<[<>()][()<>]>[(()())((){})])(<((){})[()()]><[()<>]<{}[]>>)}{{<(()){{}<>}><<{}{}>{{}()}>}\n{({([({{(<((<(()[]){()<>}>[[()<>]]))>{[<[({}()){{}<>}){<<>[]>{()<>}}><[[{}()][<><>]][[<>()]\n[<([<{<<[[(<[{{}<>}{{}[]}]<(()[])<()()>>>[{[<><>][{}{}]}])>{[{<([]())[<>{}]>{<<><>>{(){}}}}{[(<\n({{(<{((<({{([()[]](<>))({[][]}{()()})}{(<<>[]><()[]>){((){})[<><>]}}})((<{(<>{}}<(){}>}{{<>{}}{<><>}}>{(\n[({[{{([({[{<{<>[]}[[]()]>}[(({}<>){<>[]})[{{}{}}<{}()>]]]}{[{[{<>()}](<<>()>(<>()))}][<(({}\n<{([[(<[{[{(<<{}<>>(<>{})><{(){}}<{}<>>>)(({()()}([]())){<[]{}>({}<>)})}[{<[(){}][(){}]>{{<>()}<(\n{[(<<<[<{[{({[<>()]{<>[]}})[<<<>()><{}())>([[]()]((){}))]}][[{<[<>[]]<<>()>>(({}()))}](<{<<>>{<>[]\n{{{({{<[{([[(([]())<<><>>)(([]{})[[]()])]((<{}[]>{[]()}))]<{<{<>[]}(()())>({<>[]}[<><>])}(((()()){<>[]}\n<[{[([{([[<(<([][]){{}[]}>([(){}][<>]))><({<()[]>[<>()]}[([]{})])>]({{[(<><>)(<>)]{([]())}}<<{<><>}<{}()\n[[(<[[(<([([{[{}{}]{{}()}}(({}<>)<[]{}>)]{<(()())>})]({{(([]<>)[[]<>]){[<><>]{<><>}}}}[<{<<><>>[<>{\n([[(({(<({<{<[<>{}]([]{})>([{}<>]<{}{}>)}[{{[]<>}[[]{}]}]>}{([([[]{}][{}()])([<>]({}<>))])<([[{\n{[[<[({{<({[{({}<>){[]<>}}[({})([]{})]]{<{{}[]}{[]{}}>}}(((<{}>[[]<>]))<(<{}[]>([]<>))>))[[{\n<((<(([(<<[[<{()<>}<{}<>>>{<<><>>{[]<>}}]({{[]<>}[[]{}]}<(<><>)([]<>)>)]><{<[[[]{}]<[]{}>]>}<(<{<>[]\n<[[<({[[<{<[<([][]){<>[]}><((){}){()[]}>]>}(<<<{(){}}[[]()]>({[]{}}(()<>))>><[({{}{}}[[]{}])(<<>()><<>[\n[<<[[[[({<{[[{()()}<()()>]{[[][]][[]<>]}][<<<>{}>[<>]>{{<><>}}]}<{[<<>{}>{{}()}]{<{}[]>})<[(())<{}{}>]\n{{{<<({(([{{[(<>{})<<>[]>][[[]{}]{()[]}]}<<({}())>{{<>()}<{}<>>}>}]<[<[<()()>{{}()}]<([]<>)>>[([[]]<<>[]>){[\n([[[(<{(({({<[{}()]<[]{}>>[<<><>>(<><>)]}[{<<>>([]{})}([{}[]]{<><>])]){[({()()}((){}))[[[]'.strip()
test_input = '[({(<(())[]>[[{[]{<()<>>\n[(()[<>])]({[<{<<[]>>(\n{([(<{}[<>[]}>{[]{[(<()>\n(((({<>}<{<{<>}{[]{[]{}\n[[<[([]))<([[{}[[()]]]\n[{[{({}]{}}([{[{{{}}([]\n{<[[]]>}<{[{[{[]{()[[[]\n[<(<(<(<{}))><([]([]()\n<{([([[(<>()){}]>(<<{{\n<{([{{}}[<[[[<>{}]]]>[]]'.strip()


def legal_chunks(string: str) -> (bool, str, str):
    """
    returns in format (success, expected, found)
    
    expected will be a len > 1 string of the unclosed chunks if success
    found will be an empty string if success
    """
    valid = {'(': ')', '[': ']', '{': '}', '<': '>'}
    valid_keys, valid_values = valid.keys(), valid.values()

    bracket_stack: list[str] = []
    for ch in string:
        if ch in valid_keys:
            bracket_stack += ch
        elif ch in valid_values:
            if len(bracket_stack) == 0:
                return (False, '', ch)  # unexpected closing char
            elif ch == valid[bracket_stack[-1]]:
                bracket_stack.pop()
            else:
                return (False, valid[bracket_stack[-1]], ch)  # wrong closing char
    return (True, ''.join(bracket_stack[::-1]), '')

def part1(puzzle):
    corrupted_lines = [(line, legal_chunks(line)[2]) for line in puzzle.split('\n') if not legal_chunks(line)[0]]
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    return sum(points[line[1]] for line in corrupted_lines)

def part2(puzzle):
    incomplete_lines = [(line, legal_chunks(line)[1]) for line in puzzle.split('\n') if legal_chunks(line)[0]]
    points = {'(': 1, '[': 2, '{': 3, '<': 4}
    total_scores = []
    for line, completion in incomplete_lines:
        score = 0
        for ch in completion:
            score *= 5
            score += points[ch]
        total_scores.append(score)
    return statistics.median(total_scores)

print(part1(puzzle_input))
print(part2(puzzle_input))
