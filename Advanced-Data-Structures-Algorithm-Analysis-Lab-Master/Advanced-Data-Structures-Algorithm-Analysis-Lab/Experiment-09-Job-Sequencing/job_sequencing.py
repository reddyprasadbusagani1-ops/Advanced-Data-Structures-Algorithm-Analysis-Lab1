"""Job sequencing with deadlines using a greedy algorithm.

Input format in input.txt:
number_of_jobs
job_id deadline profit   (one job per line)
"""
from pathlib import Path


def job_sequencing(jobs):
    """Return scheduled jobs, total profit, and available time slots."""
    if not jobs:
        return [], 0, []

    # Greedy choice: consider jobs in descending order of profit.
    jobs_sorted = sorted(jobs, key=lambda job: job[2], reverse=True)
    max_deadline = max(max(0, job[1]) for job in jobs_sorted)
    slots = [None] * max_deadline
    total_profit = 0

    for job_id, deadline, profit in jobs_sorted:
        # A job can be placed in any free slot no later than its deadline.
        for slot in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[slot] is None:
                slots[slot] = (job_id, profit)
                total_profit += profit
                break

    schedule = [(index + 1, job[0], job[1])
                for index, job in enumerate(slots) if job is not None]
    return schedule, total_profit, slots


def read_jobs(path):
    lines = [line.strip() for line in path.read_text().splitlines()
             if line.strip() and not line.strip().startswith('#')]
    if not lines:
        raise ValueError('input.txt is empty')
    count = int(lines[0])
    jobs = []
    for line in lines[1:]:
        parts = line.split()
        if len(parts) != 3:
            raise ValueError(f'Invalid job line: {line!r}. Expected: job_id deadline profit')
        job_id, deadline, profit = parts[0], int(parts[1]), int(parts[2])
        if deadline < 0:
            raise ValueError('Deadlines must be zero or positive')
        jobs.append((job_id, deadline, profit))
    if len(jobs) != count:
        raise ValueError(f'Expected {count} jobs, but found {len(jobs)}')
    return jobs


def main():
    folder = Path(__file__).resolve().parent
    input_path = folder / 'input.txt'
    output_path = folder / 'output.txt'
    try:
        jobs = read_jobs(input_path)
        schedule, total_profit, _ = job_sequencing(jobs)
        result = [
            'Job Sequencing with Deadlines (Greedy Algorithm)',
            f'Total jobs: {len(jobs)}',
            'Scheduled jobs (time slot, job ID, profit):',
        ]
        if schedule:
            result.extend(f'Slot {slot}: Job {job_id} (Profit: {profit})'
                          for slot, job_id, profit in schedule)
        else:
            result.append('No jobs scheduled.')
        result.append(f'Total profit: {total_profit}')
        result_text = '\n'.join(result) + '\n'
        print(result_text, end='')
        output_path.write_text(result_text)
        print(f'Results saved to {output_path.name}')
    except (ValueError, OSError) as error:
        print(f'Error: {error}')
        raise SystemExit(1)


if __name__ == '__main__':
    main()
