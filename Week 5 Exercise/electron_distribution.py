# The basic idea of electron distribution is that electrons should fill a shell until it holds the maximum number of electrons.
# You will receive a single integer - the number of electrons. Your task is to fill shells until there are no more electrons left.
# The rules for electron distribution are as follows:
#     • The maximum number of electrons in a shell can be 2n2, where n is the position of a shell (starting from 1).
#     For example, the maximum number of electrons in the 3rd shield can be 2*32 = 18.
#     • You should start filling the shells from the first one at the first position.
#     • If the electrons are enough to fill the first shell, the left unoccupied electrons should fill the following shell and so on.
# In the end, print a list with the filled shells.

electrons = int(input())
shell = 0
shell_list = []

while electrons > 0:
    shell += 1
    maximum_electrons_in_a_shell = 2 * (shell ** 2)
    if maximum_electrons_in_a_shell < electrons:
        electrons -= maximum_electrons_in_a_shell
        shell_list.append(maximum_electrons_in_a_shell)
    else:
        shell_list.append(electrons)
        electrons = 0

print(shell_list)



