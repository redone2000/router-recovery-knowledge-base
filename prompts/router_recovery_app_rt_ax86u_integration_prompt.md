# Router Recovery App Prompt: RT-AX86U Reviewed-Candidate Integration

Use this prompt in the Router Recovery macOS App project thread, not in the knowledge-system thread.

```text
请继续 Router Recovery macOS App 项目，但先遵守 App 项目自己的审核状态边界。

App 项目路径：

/Users/YiYuan/Documents/本地Xcode/Tftp Server

请先执行：
1. 阅读 AGENTS.md。
2. 运行 git status --short --branch。
3. 阅读 HANDOFF.md 和 PROJECT_STATUS.md。
4. 以 App 项目当前文件、git 状态、App Store Connect 当前状态为准，不要依赖旧聊天历史。

重要边界：
- 如果 Router Recovery 2.1.0 build 25 仍在 App Store Review 等待期，不要主动改 App 二进制、截图、元数据、IAP、定价、签名、Archive、Upload、Submit 或 Release。
- RT-AX86U reviewed-candidate slice 只能作为后续 build 的候选输入，不应干扰当前审核中的 build 25。
- 任何 Archive / Upload / Submit / Release / App Store Connect 操作必须先获得用户明确确认。

知识库输入来源：

/Users/YiYuan/Projects/router-recovery-knowledge

请只读取这些文件作为 RT-AX86U 后续实现输入：
- reports/rt_ax86u_app_integration_slice_2026-05-26.md
- app_exports/examples/asus_rt_ax86u_app_profile_draft.json
- schema/app_runtime_attempt.schema.json
- docs/app_upgrade_field_contract.md
- docs/app_recovery_runtime_workflow.md

核心事实：
- RT-AX86U 当前只是 reviewed candidate，不是 final。
- source_profile_status = reviewed。
- production_allowed = false。
- final_allowed = false。
- review_required = true。
- 不要把它展示成 officially supported / final / general RT-AX86U support。

实现目标：
为后续 build 准备一个最小、证据边界清晰的 App 集成方案，让 App 能消费 reviewed-candidate export，而不是扩大支持型号。

如果当前 App 仍在审核等待期，推荐只产出实现计划或待办文档，不写代码。计划应说明：
1. 哪些 App 文件未来需要修改。
2. 如何加载 reviewed-candidate JSON。
3. 如何在 UI 中显示 reviewed-candidate / observation-only / not-final 状态。
4. 如何保留 upload complete 与 recovery complete 的状态分离。
5. 如何记录 runtime attempt，并保持本地私有、路径/序列号/MAC/固件文件脱敏。
6. 哪些行为明确不做：final profile、自动固件下载、存储固件二进制或本地路径、承诺配置保留、泛化到 stock ASUSWRT 或其它硬件版本。

必须保留的 RT-AX86U 行为边界：
- 设备：ASUS RT-AX86U，H/W Ver. 1.0。
- 固件证据：ASUSWRT-Merlin 3004.388.11 -> 3004.388.10_2 的一次测试。
- Rescue Mode entry：Reset-held power-on、LAN1、慢闪 power LED、192.168.1.1 TTL=100。
- Web recovery 未观察到。
- 使用 Passive TFTP PUT。
- Mac/App 是 TFTP client；router 是 TFTP server。
- WRQ/PUT 到 192.168.1.1:69。
- ACK block 0 来自 192.168.1.1:69；未观察到 ephemeral server port。
- 上传完成后不是恢复完成。
- 等待数分钟后，DHCP/admin 未自动返回，正常断电重启后才回到 DHCP/admin。
- 配置保留只是一台设备的一次观察，不可承诺。

必须避免：
- 不要把 ping/TTL 单独当作恢复成功或可恢复证明。
- 不要把 transfer complete 写成 recovery success。
- 不要在 transfer complete 后立即引导断电。
- 不要实现 router-pulls-firmware / active TFTP for this profile。
- 不要合并 RT-AX86U 和 RT-AC86U。
- 不要泛化到 stock ASUSWRT、其它地区、其它硬件版本或其它 firmware family。

建议验收标准：
1. 能读取 asus_rt_ax86u_app_profile_draft.json。
2. 明确拒绝把 reviewed candidate 当作 final。
3. UI 能显示风险摘要或要求用户确认完整风险范围。
4. runtime attempt 字段能覆盖 schema/app_runtime_attempt.schema.json 需要的关键事实。
5. transfer_complete 与 recovery_success 分开。
6. post-upload wait、power cycle、DHCP return、admin UI check、firmware verification 分开记录。
7. 导出的 runtime attempt JSON 可回到知识库用 tools/validate_runtime_attempts.py 验证。
8. runtime result 不自动写回或修改 model profiles。

如果 App Review 反馈已经到达：
- 先处理 App Review 的精确反馈。
- RT-AX86U 后续集成只有在不影响拒审修复最小路径时才继续。
```

