from typing import List, Callable
from fin import Node, FinParams

def balance(nodes: List[Node],
            params: FinParams,
            k_of_T: Callable[[float], float]) -> int:
    """就地更新 nodes 的温度，返回迭代步数"""
    dx, P, A = params.geometry()
    current_step = 0

    while True:
        current_step += 1
        tol_count = 0
        max_error = 0.0

        # 内部/末端节点（0 为固定边界）
        for i in range(1, params.total_node):
            Ti  = nodes[i].T
            Tm1 = nodes[i-1].T

            # 左导热
            k_left = k_of_T(0.5*(Tm1 + Ti))
            Q_left = k_left * A/dx * (Tm1 - Ti)

            # 对流
            conv = params.hc * P * dx * (params.Ta - Ti)

            if i <= params.total_node - 2:
                # 右导热
                Tp1 = nodes[i+1].T
                k_right = k_of_T(0.5*(Ti + Tp1))
                Q_right = k_right * A/dx * (Tp1 - Ti)
                summ = Q_left + Q_right + conv
            else:
                # 末端：绝热端近似（不含端面对流）
                summ = Q_left + conv

            # 残差下降更新
            Ti_new = Ti + params.delta * summ
            if Ti_new > params.T0: Ti_new = params.T0
            if Ti_new < params.Ta: Ti_new = params.Ta
            nodes[i].T = Ti_new

            # 收敛统计
            ares = abs(summ)
            if ares <= params.error:
                tol_count += 1
            if ares > max_error:
                max_error = ares

        if params.print_step and current_step % params.print_step == 0:
            print(f"step={current_step}, max_error={max_error:.6f}, pass={tol_count}/{params.total_node-1}")
            if tol_count == (params.total_node - 1) or current_step >= params.max_step:
                return current_step