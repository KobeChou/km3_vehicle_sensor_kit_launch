# 在 Autoware 中集成/更新 km3_vehicle_sensor_kit_launch

## 方式一：通过 .repos 文件（推荐）

### 1. 创建或编辑 Autoware 工作空间的 .repos 文件

在 Autoware 工作空间根目录（或 `src` 目录）创建 `km3_sensor_kit.repos`：

```yaml
repositories:
  km3_vehicle_sensor_kit_launch:
    type: git
    url: <你的仓库地址>   # 例如: https://github.com/xxx/km3_vehicle_sensor_kit_launch.git
    version: main         # 或你的分支名
```

**使用本地路径**（开发时常用）：
```yaml
repositories:
  km3_vehicle_sensor_kit_launch:
    type: git
    url: file:///d:/mksoft/2025/driver_exam/code4/km3_vehicle_sensor_kit_launch
    version: main
```

### 2. 导入仓库

```bash
cd /path/to/autoware_ws
vcs import src < km3_sensor_kit.repos
# 若已有 autoware.repos，可追加导入：
# vcs import src < autoware.repos
# vcs import src < km3_sensor_kit.repos
```

### 3. 更新仓库

```bash
cd /path/to/autoware_ws
vcs pull src    # 拉取所有 .repos 中的仓库更新
# 或只更新本仓库：
cd src/km3_vehicle_sensor_kit_launch
git pull origin main
cd ../..
```

### 4. 编译

```bash
cd /path/to/autoware_ws
source /opt/ros/humble/setup.bash   # 或你的 ROS2 版本
colcon build --packages-select km3_vehicle_sensor_kit_launch km3_vehicle_sensor_kit_description common_sensor_launch
# 或全量编译：
colcon build --symlink-install
source install/setup.bash
```

---

## 方式二：直接克隆到 src

```bash
cd /path/to/autoware_ws/src
git clone <你的仓库地址> km3_vehicle_sensor_kit_launch
cd ..
colcon build --packages-select km3_vehicle_sensor_kit_launch km3_vehicle_sensor_kit_description common_sensor_launch
source install/setup.bash
```

**更新**：
```bash
cd src/km3_vehicle_sensor_kit_launch
git pull
cd ../..
colcon build --packages-select km3_vehicle_sensor_kit_launch km3_vehicle_sensor_kit_description common_sensor_launch
source install/setup.bash
```

---

## 方式三：覆盖 sample_sensor_kit_launch（若 Autoware 引用它）

若 Autoware 的 vehicle launch 引用的是 `sample_sensor_kit_launch`，可：

1. **在 .repos 中覆盖**：将 `sample_sensor_kit_launch` 的 path 指向你的仓库
2. **或修改 Autoware vehicle 配置**：把 sensing launch 的包名改为 `km3_vehicle_sensor_kit_launch`

---

## 依赖说明

本仓库依赖（需在 Autoware 工作空间中存在）：
- `autoware_pointcloud_preprocessor`
- `autoware_imu_corrector`
- `autoware_gnss_poser`
- `autoware_vehicle_velocity_converter`
- `common_sensor_launch`（本仓库内）
- `ws_30pcd_et3_ros2`（你的雷达驱动）

`build_depends.repos` 中列出的依赖需先导入：
```bash
vcs import src < build_depends.repos
```

---

## 启动

```bash
source install/setup.bash
ros2 launch km3_vehicle_sensor_kit_launch sensing.launch.xml
```
