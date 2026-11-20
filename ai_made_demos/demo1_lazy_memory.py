"""Demo 1: virtual memory is lazy. Asking for memory is not the same as using RAM."""
import mmap
import resource


def mem():
    """Read this process's memory numbers straight from the OS (Linux)."""
    vals = {}
    with open("/proc/self/status") as f:
        for line in f:
            if line.startswith(("VmSize", "VmRSS")):
                key, value = line.split(":")
                vals[key] = int(value.split()[0]) // 1024  # kB -> MB
    faults = resource.getrusage(resource.RUSAGE_SELF).ru_minflt
    return f"virtual={vals['VmSize']:>5} MB | real RAM (RSS)={vals['VmRSS']:>4} MB | page faults={faults}"


PAGE = mmap.PAGESIZE
SIZE = 500 * 1024 * 1024  # 500 MB

print("page size:", PAGE, "bytes")
print("start         :", mem())

buf = mmap.mmap(-1, SIZE)  # ask the OS for 500 MB of anonymous memory
print("asked 500 MB  :", mem())  # virtual jumps, RSS barely moves

for off in range(0, SIZE // 2, PAGE):  # write 1 byte into every page of the first half
    buf[off] = 1
print("touched 250 MB:", mem())  # now RSS grows, and so do page faults

for off in range(SIZE // 2, SIZE, PAGE):
    buf[off] = 1
print("touched 500 MB:", mem())

buf.close()
print("freed         :", mem())

# The address split from your homework, done in code:
address = 20000
print(f"\naddress {address}: page number={address // PAGE}, offset={address % PAGE}")
