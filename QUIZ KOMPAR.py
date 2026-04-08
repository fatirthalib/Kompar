import random
import heapq

# =========================
# INPUT NRP
# =========================
NRP = "152020110"  # ganti sesuai kebutuhan

# =========================
# CONFIG
# =========================
NUM_WORKERS = 4
NUM_TASKS = 20
random.seed(42)

# Generate task (beban tidak merata)
tasks = [random.randint(1, 10) for _ in range(NUM_TASKS)]

total_work = sum(tasks)
ideal_load = total_work / NUM_WORKERS

print("=" * 50)
print(f"NRP: {NRP}")
print(f"Tasks: {tasks}")
print(f"Total Work: {total_work}")
print(f"Ideal Load per Worker: {ideal_load:.2f}")
print("=" * 50)


# =========================
# STATIC UNEVEN DISTRIBUTION
# =========================
def static_uneven(tasks, num_workers):
    workers = [[] for _ in range(num_workers)]

    # pembagian tidak merata (round robin sederhana)
    for i, task in enumerate(tasks):
        workers[i % num_workers].append(task)

    loads = [sum(w) for w in workers]

    print("\n[STATIC UNEVEN DISTRIBUTION]")

    for i in range(num_workers):
        print(f"Worker {i}: Load = {loads[i]}, Tasks = {workers[i]}")

    max_load = max(loads)
    print(f"Completion Time: {max_load}")

    # cek apakah mendekati ideal
    tolerance = 0.1 * ideal_load
    if all(abs(load - ideal_load) <= tolerance for load in loads):
        print("Status: Mencapai IDEAL distribution")
    else:
        print("Status: TIDAK ideal (imbalanced)")

    return max_load


# =========================
# DYNAMIC DISTRIBUTION
# =========================
def dynamic_distribution(tasks, num_workers):
    print("\n[DYNAMIC DISTRIBUTION]")

    # min heap (load terkecil selalu diprioritaskan)
    heap = [(0, i) for i in range(num_workers)]
    heapq.heapify(heap)

    assignment = {i: [] for i in range(num_workers)}

    for task in tasks:
        load, wid = heapq.heappop(heap)

        load += task
        assignment[wid].append(task)

        heapq.heappush(heap, (load, wid))

    final_loads = [load for load, _ in heap]

    for i in range(num_workers):
        print(f"Worker {i}: Load = {sum(assignment[i])}, Tasks = {assignment[i]}")

    max_load = max(final_loads)
    print(f"Completion Time: {max_load}")
    print("Status: Mendekati waktu optimal")

    return max_load


# =========================
# MAIN LOGIC (BERDASARKAN NRP)
# =========================
last_digit = int(NRP[-1])

if last_digit % 2 == 0:
    print("\nNRP GENAP → Menggunakan STATIC UNEVEN DISTRIBUTION")
    static_time = static_uneven(tasks, NUM_WORKERS)

    print("\n(Opsional Perbandingan dengan Dynamic)")
    dynamic_time = dynamic_distribution(tasks, NUM_WORKERS)

    print("\nPerbandingan:")
    print(f"Static  : {static_time}")
    print(f"Dynamic : {dynamic_time}")
    print(f"Selisih : {static_time - dynamic_time}")

else:
    print("\nNRP GANJIL → Menggunakan DYNAMIC DISTRIBUTION")
    dynamic_time = dynamic_distribution(tasks, NUM_WORKERS)

    print(f"\nExpected Optimal Time ≈ {ideal_load:.2f}")