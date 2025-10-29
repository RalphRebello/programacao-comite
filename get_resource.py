#!/usr/bin/env python3
import subprocess
from openpyxl import Workbook
from datetime import datetime


def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True, text=True)


def parse_resource(value):
    """Converte o valor de CPU/memória para cores e GiB."""
    if value.endswith('m'):  # milicores
        return float(value[:-1]) / 1000  # retorna em cores
    elif value.endswith('n'):  # nanocores
        return float(value[:-1]) / 1e9
    elif value.endswith('Ki'):
        return float(value[:-2]) / (1024 * 1024)
    elif value.endswith('Mi'):
        return float(value[:-2]) / 1024
    elif value.endswith('Gi'):
        return float(value[:-2])
    else:
        try:
            return float(value)
        except ValueError:
            return 0.0


def main():
    # Coleta métricas de todos os pods
    top_output = run_cmd("kubectl top pods --all-namespaces --no-headers")

    usage = {}

    for line in top_output.splitlines():
        parts = line.split()
        if len(parts) < 4:
            continue

        namespace = parts[0]
        cpu_usage = parts[2]
        mem_usage = parts[3]

        cpu_cores = parse_resource(cpu_usage)   # cores
        mem_gib = parse_resource(mem_usage)     # GiB

        if namespace not in usage:
            usage[namespace] = {"pods": 0, "cpu_cores": 0.0, "mem_gib": 0.0}

        usage[namespace]["pods"] += 1
        usage[namespace]["cpu_cores"] += cpu_cores
        usage[namespace]["mem_gib"] += mem_gib

    # === Exibe no terminal em milicpu ===
    print(f"{'Namespace':20s} {'Pods':>6s} {'CPU (m)':>10s} {'Memory (GiB)':>15s}")
    print("-" * 55)
    for ns, vals in usage.items():
        cpu_m = vals["cpu_cores"] * 1000  # cores → milicpu
        print(
            f"{ns:20s} {vals['pods']:6d} {cpu_m:10.0f} {vals['mem_gib']:15.2f}")

    # === Planilha Excel ===
    wb = Workbook()
    ws = wb.active
    ws.title = "K8s Namespace Usage"

    ws.append(["Namespace", "Pods", "CPU (m)", "Memory (GiB)"])

    for ns, vals in usage.items():
        cpu_m = vals["cpu_cores"] * 1000
        ws.append([ns, vals["pods"], round(
            cpu_m, 0), round(vals["mem_gib"], 2)])

    # Totais
    total_pods = sum(v["pods"] for v in usage.values())
    total_cpu_m = sum(v["cpu_cores"] for v in usage.values()) * 1000
    total_mem = sum(v["mem_gib"] for v in usage.values())
    ws.append(["TOTAL", total_pods, round(
        total_cpu_m, 0), round(total_mem, 2)])

    filename = f"k8s_namespace_usage_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    wb.save(filename)

    print(f"\n✅ Dados salvos em: {filename}")


if __name__ == "__main__":
    main()
