from mpi4py import MPI


comm    =   MPI.COMM_WORLD
rank    =   comm.Get_rank()
size    =   comm.Get_size()
summa = comm.reduce(rank,op=MPI.SUM,root = 0)

if rank == 0:
    print(summa)