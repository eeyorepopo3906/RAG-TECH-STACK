---
theme: ./themes/linktimecloud-productmarketing
layout: cover
class: text-center
title: KDP OEM PPT
version: 3.0
---

# Kubernetes 
# Data Platform

K8s大数据平台（KDP）

---
layout: intro
---

# 目录

contents

产品概述

技术架构

功能特性

操作界面

使用场景

部署维护

---
layout: intro
---

# 产品概述

Product Overview

01 产品定位

02 目标用户

03 核心功能

---
layout: items
---

## 01 产品定位

Kubernetes Data Platform K8s 大数据平台，简称 KDP。

KDP 是一个基于容器、K8s 和大数据技术的大数据平台产品，利用云原生的资源隔离、作业混排、存算分离、标准化部署运维等技术优势，解决传统大数据平台资源利用率低、部署运维复杂、难以弹性扩容等技术难题，帮助用户花更少时间、用更少的资源去进行大数据平台的部署、配置和运维。

---
layout: items
---

## 02 目标用户

复杂应用程序和基础架构企业

* 画像：拥有大规模、高可用性和弹性伸缩要求的应用程序，可能已经采用了云原生技术栈。
* 核心需求：需要提高资源利用效率，存算分离、急用急走。响应国家政策，需要使用国产化云原生技术。需要降低运维成本，自动化解决大部分性能问题，标准化方式统一管理。对安全性和访问控制有严格要求，需要确保应用程序和数据的安全性。
* 期望：选择一个能降本增效自主可控的Kubernetes大数据平台，简化应用程序的部署和管理，能提供大规模、高可用性和弹性伸缩功能，授权鉴权完备，安全性高。

---
layout: items
---

## 02 目标用户

技术赋能业务企业

* 画像：具备较高的技术能力和经验，熟悉容器和云原生概念，能够管理和维护分布式系统。
* 核心需求：自动化部署和扩展应用程序，滚动更新，以适应不断变化的业务需求。面临容错和故障恢复的挑战，能快速恢复运行。需要全面监控和记录应用程序的运行状态和日志，以便及时进行问题定位和解决。
* 期望：选择一个易于使用和管理的Kubernetes大数据平台，跟上技术转变浪潮，提供自动化部署、滚动更新、容错和故障恢复、监控和日志、安全和访问控制等功能，能满足复杂的业务需求，并提升开发、部署和维护效率。

---
layout: items
---

## 03 核心功能

K8s标准集成基座

KDP的主要功能是提供了一个标准的集成基座，将成熟的开源大数据组件以标准化的方式集成到K8s平台上，确保它们可以按云原生的方式部署，运行和运维。

* 标准流程

### 形成标准的云原生大数据组件集成流程，将开源大数据组件与统一系统服务对接，形成标准化配置文件

* 统一操作

### 通过配置文件来完成大数据组件到K8s集群的发布、更新、运维、升级操作

* 可观测性

### 提供大数据组件的可观测性服务，包括大数据组件日志、性能及稳定性的指标监控和报警，计费以及审计功能

* 调度支持

### 为计算大数据计算引擎提供云原生的调度机制支持，提升资源使用率与运行效率

---
layout: items
---

## 03 核心功能

<div grid="~ cols-2 gap-4 ">
<div class="text-left">

大数据组件K8s改造
  
* 在标准集成基座的基础上，KDP集成了主流的大数据计算和存储引擎，所有大数据组件均以容器的方式运行在K8s系统之上。
* 在集成这些大数据组件的过程中，我们保留了其原生的访问方式（UI、接口、协议等），但是通过对开源代码的修改和扩展，强化了标准化的部署和运维、统一的可观测性、统一的安全认证和鉴权机制、以及性能上的优化。
</div>
<div  class="text-left">
  <img src="/image_slides/slides-2023-10-18-17-37-05.png" /> 
</div>
</div>

---
layout: items
---

## 03 核心功能

组件K8s性能优化

虽然K8s对有状态服务的支持逐渐在加强，但是很多大数据组件直接在K8s上运行时会有性能上的问题。
我们要确保各种大数据组件在K8s上的运行性能，利用云原生的机制来提升组件性能，减少由于容器化和插件化带来的性能损耗，处理各种特性的大数据工作负载。

* Hive On Spark On Kubernetes
  * Hive Metastore和Hive Server2实现了高可用和负载平衡，Hive查询作业将会转化成 Spark 作业在 K8s 中运行，支持部署多个Hive Server2实例将Hive作业的请求进行分流
* Spark on Kubernetes Operator
  * 对 Spark 计算引擎做了相应优化，一是解决了云原生环境下的 Data locality 问题，二是通过持续运行机制避免了 Spark pod 的频繁启动
* Flink
  * 纳入统一调度引擎，实现了跟其他云原生大数据组件的对接

---
layout: items
---

## 03 核心功能

<div class="text-left text-base py-2">

集成管理运维平台 -- KDP允许用户在一个统一的界面里发布新的组件，查看组件运行情况，资源使用情况，运行日志，大大降低了运维的难度，提高了运维的效率
</div>

<img class="h-85 mx-auto shadow" src="/image_slides/slides-2023-11-02-10-41-45.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);" />

---
layout: intro
---

# 技术架构

Technical Architecture

04 传统大数据的限制

05 云原生趋势

06 KDP 系统架构

07 KDP 技术突破

08 KDP 技术优势

09 国产软硬件支持

---
layout: items
---

## 04 传统大数据平台的限制

<div class="h-4"></div>

<div class="grid gap-x-8 gap-y-4 grid-cols-2">
 <div class="grid gap-2 grid-cols-2">
  <div>
  1、安装复杂

### 各个组件都是独立安装流程，需要很多软硬件适配，手工配置文件修改，在安装过程中需要人工状态检查及同步协调，难以自动化自助化。

  </div>
  <div>

  <img class="h-45 mx-auto" src="/image_slides/traditional_install.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);" />

  </div>

  </div>

 <div class="grid gap-4 grid-cols-2">
  <div>
  2、运行效率难以提升

### 系统的大部分计算还依赖于传统Yarn引擎和MapReduce，难以统一计算引擎调度，利用社区进展，提升计算引擎效率。

  </div>
  <div>

  <img class="h-45 mx-auto" src="/image_slides/traditional_operating_efficiency.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);" />

  </div>

  </div>

 <div class="grid gap-4 grid-cols-2">
  <div>
  3、资源利用率低

### 各个组件都是事先分配资源，无法共享资源池，或者动态根据负载调整组件的资源分配，造成资源分散，隔离度高，闲置率高。

  </div>
  <div>

  <img class="h-45 mx-auto" src="/image_slides/traditional_resource_efficiency.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

  </div>

  </div>

 <div class="grid gap-4 grid-cols-2">
  <div>
  4、运维难度大

### 各个组件都是独立运维，网络存储方案难以统一，运维复杂，对运维人员要求高，常规运维操作难以自动化。

  </div>
  <div>

  <img class="h-45 mx-auto" src="/image_slides/traditional_maintain.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

  </div>

  </div>

</div>

---
layout: items
---

## 04 传统大数据平台的限制

<div class="h-4"></div>

<div grid="~ cols-2 gap-4">
<div class="text-left">

5、 难以实现资源的隔离

### 多租户环境下的数据开发效率提升，需要以资源隔离的方式来保证租户之间的计算作业互相不影响，特别是不能出现某一个或几个租户独占集群资源的情况

7、 Hadoop存算合一的紧耦合架构决定了它的资源利用率无法提高

### 在一个Hadoop集群中，一个节点既是存储节点（data node）， 也是计算节点。 当存储资源不够的时候， 增加节点可以进行存储扩容， 但会造成计算资源的利用率下降；同样，当计算资源不够而进行扩容的时候，存储资源利用率就会下降

</div>
<div class="text-left">

6、难以集成新的计算和存储技术

### Hadoop系统在部署其他组件的时候，对这些组件与HDFS和Yarn的版本适配有严格要求。引入一个新的计算和存储组件的难度是非常高的

8、Hadoop集群资源无法做到快速的弹性扩容和缩容

### Hadoop的节点扩容和缩容流程，导致扩缩容无法在很快的时间内完成，数据备份以较小的传输率运行在后台，往往要持续几个小时
  
</div>
</div>

传统大数据平台因为其结构性的缺陷导致了多租户环境下数据开发效率低、集群资源利用率不高以及集成新技术很复杂等问题，依靠Hadoop生态技术框架本身的发展是不可能解决这些问题的。

---
layout: items
---

## 05 云原生趋势

Kubernetes作为云原生时代的“操作系统”，已于2021年3月和5月分别正式支持Spark on K8s、Kafka on K8s，HDFS也有了云原生的对标方案，大数据平台的云原生化已是大势所趋。随着 K8s 的进一步成熟和工具链的完善，我们相信越来越多的大数据应用会以云原生的方式发布。如何利用新的云原生体系提升大数据系统的效率，是每个希望高效完成数字化转型的企业需要回答的问题。

<img class="h-70 mx-auto" src="/image_slides/slides-2023-10-18-15-22-09.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

---
layout: items
---

## 05 云原生趋势

<div grid="~ cols-2 gap-4">

<div class="text-left">

<div class="h-6"></div>

<img class="h-22 w-90 mx-auto" src="/image_slides/cloudnative_gartner.jpg" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

<img class="h-32 w-90 mx-auto" src="/image_slides/cloudnative_gartner2.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

### * 据 Gartner 预测，部署在云原生平台上的数字工作负载将由 2021 年的 30%增长至 2025 年的 95%
### * Spark, Kafka等大数据核心组件，2021年开始K8s原生支持
### * 2022年6月，阿里云和腾讯云的云原生数据湖产品均通过了中国信息通信研究院首批云原生数据湖能力评测
### * 美国苹果公司在2022年的一次技术大会上透露，Apple的云原生大数据平台每天运行38万个Spark作业

</div>

<div class="text-left">

<img class="h-75 mx-auto" src="/image_slides/slides-2023-12-28-16-51-09.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

### 在华为2022年9月发布的《云原生2.0白皮书》中，数据应用和业务应用会在统一的云原生基础设施上以云原生形态运行。Databricks / Cloudera等头部企业主要底层平台已经在往Kubernetes迁移，例如，Spark的缺省调度引擎将会迁移到基于Kubernetes的Volcano和Yunicorn上，而对Yarn的支持会逐渐退出主流解决方案。

</div>

</div>

---
layout: items
---

## 06 KDP 系统架构

<img class="h-100 mx-auto mt-5" src="/image_slides/KDP-architecture-diagram.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

---
layout: items
---

## 07 KDP 技术突破

<br>

<div grid="~ cols-2 gap-4">

<div class="text-left">

* 组件代码级云原生化
  
### 对大数据核心组件进行代码级别的改造以支持K8s 资源调度，网络及存储体系，并将这些组件的最新版本进行统一集成

</div>

<div class="text-left">

* 实现多租户管理

### 利用K8s的命名空间实现多租户管理，资源隔离，实现按需动态资源配置，并实现了资源使用统计计费组件

</div>

<div class="text-left">

* 组件运维自动化

### 在大数据组件的Operator和Helm Chart之上创建了统一抽象层，实现发布和运维的标准化和自动化

</div>

<div class="text-left">

* 实现 Infra as Code

### 基于OAM标准统一应用发布和管理流程，打通各组件之间的配置管理，实现Infra as Code

</div>

<div class="text-left">

* 强化认证及鉴权机制

### 扩展并强化了多租户环境下的安全认证及鉴权机制，采用统一的Kerberos安全认证和基于Ranger的授权机制

</div>

<div class="text-left">

* 优化计算引擎性能

### 对计算引擎在云原生形态下的性能进行优化，例如：批流作业统一的Volcano调度，解决了Spark on HDFS的Data Locality问题

</div>

</div>

---
layout: items
---

## 08 KDP 技术优势

<div grid="~ cols-2 gap-4">

<div class="text-left">

更高的集群资源利用率

### KDP可以帮助我们的客户，从传统大数据平台30%左右的资源利用率，提升到60%以上

</div>

<div class="text-left">

更高效的集群运维

### KDP通过标准化流程简化了大数据集群的运维，并提供UI界面进一步提升了部署、升级等操作的效率

</div>

<div class="text-left">

更容易集成新的大数据组件

### KDP提供标准化自动化的大数据组件部署和运维，极大地缩短了大数据项目开发和上线时间

</div>

<div class="text-left">

更好的大数据计算性能

### KDP通过统一的批流作业调度，进一步提升离线和实时处理作业的计算性能

</div>

</div>

---
layout: items
---

## 09 国产化

<br>

KDP是智领云公司自主研发的自主可控的云原生大数据平台，同时支持国产多云、混合云部署

<div class="absolute left-40">

* 公有云私有化部署

### <<<< 支持阿里云容器服务、 腾讯云TKE服务、 华为云CCE服务
### <<<< 支持私有云部署，支持在用户提供的K8s集群环境上进行部署

* 操作系统

### <<<< 中标和银河麒麟操作系统

* 服务器

### <<<< 飞腾和鲲鹏芯片的国产Arm架构CPU服务器，华为、浪潮、新华三等多家国内服务器软硬件适配

* 数据库

### <<<< 达梦、人大金仓、TiDB等

</div>

---
layout: intro
---

# 功能特性

Functionality Features

10 系统集成框架

11 应用发布服务

12 可观测性服务集成

13 调度服务集成

14 计算及存储引擎

15 多租户和安全管理

---
layout: items
---

## 10 系统集成框架

<div class="text-left">

KDP的主要功能是提供了一个标准的集成基座，将成熟的开源大数据组件以标准化的方式集成到K8s平台上，确保它们可以按云原生的方式部署，运行和运维。

<div class="px-10">

* 标准流程

### 形成标准的云原生大数据组件集成流程，将开源大数据组件与统一系统服务对接，形成标准化配置文件，标准化ConfigMap, secret等系统配置组件的发布和配置方式

<br>

* 统一对接

### 在K8s配置的基础上提供封装，简化大数据组件的配置流程，标准化组件与系统服务及其它组件之间的对接机制。提供日志，监控报警运维插件配置，隐藏底层系统细节，自动化简化配置

<br>

* 灵活配置

### 提供灵活的发布配置管理，允许用户指定namespace发布，以及依赖组件的指定，如有依赖外部系统，可从系统变量中读取依赖系统访问地址及配置，无需hardcode

</div>
</div>

---
layout: items
---

## 11 应用发布服务

<div class="h-6"></div>

<div grid="~ cols-2 gap-4">

<div class="text-left">

实现大数据组件从配置文件到K8s集群的统一发布、更新、运维与升级。

### * 实现infra-as-code的发布运维方式，所有操作以修改配置文件的方式并以control loop的方式实现

### * 负责有依赖关系的组件之间的发布流程，无需手动处理

### * 系统组件和租户体系的集成，确保授权，鉴权，权证的发布以云原生的方式完成

### * 租户的管理，实现机构/用户以及其相关资源的生命周期管理

### * 根据负载情况实现动态扩容降容

</div>
<div class="text-left">

<img class="h-80 mx-auto" src="/image_slides/slides-2023-11-02-10-41-46.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

</div>
</div>

---
layout: items
---

## 12 可观测性服务集成

<div grid="~ cols-2 gap-4">
<div>

* 日志聚合

### 提供所有大数据组件包括 batch/streaming Workload 的日志，对性能及稳定性的指标进行监控和报警，并通过统一界面进行日志管理。

* 监控报警

<div >

### 将 Prometheus 和 Grafana 容器化发布，通过大数据集成基座，实现了大数据组件部署发布流程与监控报警系统 Prometheus 和 Grafana 进行自动地对接

### * 监控：配置组件核心运维指标以及采集方式，对于batch/streaming workload，需要采取push的方式采集指标

### * 报警：根据指标设置合理的报警条件及优先级

### * 异常检测：根据运维指标自动发现异常

</div>

* 计费审计

### 收集大数据计算引擎和存储引擎的资源使用数据，对其进行整理、存储和分析，提供 HTTP API，让用户能清晰地看到各安全组、各用户、各计算作业等维度的资源使用情况的统计，并通过运维管理界面进行查询和审计

</div>
<div>
<img class="h-90 mx-auto mt-5" src="/image_slides/slides-2023-11-02-10-41-49.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>
</div>
</div>

---
layout: items
---

## 13 调度服务集成
<br>
<div grid="~ cols-3 gap-4">
<div class="text-left">

* 支持大量batch和streaming job的调度
* 支持租户隔离与弹性资源分配
* 支持云原生环境下data locality
* 支持智能化，自动的资源参数设置
* 支持不同的抢占，优先级策略
* 与现有的各种工具进行对接，满足SLA和资源使用的要求。
</div>
<div class="text-left col-span-2">

<img class="h-90 mx-auto" src="/image_slides/groupList.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

</div>
</div>

---
layout: items
---

## 14 计算及存储引擎改造与集成

<br>

<div class="grid grid-cols-2 gap-4">

<div grid="~ cols-5 gap-4">
<div class="text-left">
<img class="h-13" src="/image_slides/slides-2023-12-28-18-01-21.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>
</div>
<div class="text-left col-span-4">

* Hive：3.1.3

### （Latest Release Version: 4.0.0）
###  * 扩展开源代码支持Hive SQL以Spark作业方式运行
###  * 支持在Hue或者Beeline客户端运行Hive SQL
###  * Hive Table可以存储在HDFS或者对象存储中
</div>
</div>

<div grid="~ cols-5 gap-4">
<div class="text-left">

<img class="h-13" src="/image_slides/slides-2023-12-28-18-12-08.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

</div>
<div class="text-left col-span-4">

* Spark：3.3.0

### （Latest Release Version: 3.3.2）
###  * 扩展了Google Cloud Platform的Spark Operator
###  * 支持通过自研API或者JupyterLab运行Spark作业
###  * 扩展开源代码进行性能优化：Data Locality in HDFS、Sticky Sessions
</div>
</div>

<div grid="~ cols-5 gap-4">
<div class="text-left">
<img  class="h-13" src="/image_slides/slides-2023-12-28-18-23-55.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>
</div>
<div class="text-left col-span-4">

* Hbase 2.2.4

### （Latest Release Version: 2.5.5）
###  * 与容器化HDFS集成部署
###  * 实现Kerberos和Ranger的集成
</div>
</div>

<div grid="~ cols-5 gap-4">
<div class="text-left">
<img  class="h-13" src="/image_slides/slides-2023-12-28-18-24-32.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>
</div>

<div class="text-left col-span-4">

* Flink：1.14.6

### （Latest Release Version: 1.16.1）
###  * 扩展了Apache社区的Flink Operator
###  * Flink作业与Spark作业使用统一的调度
</div>
</div>

</div>

---
layout: items
---

## 14 计算及存储引擎改造与集成

<br>

<div class="grid grid-cols-2 gap-4">

<div grid="~ cols-5 gap-4">
<div class="text-left">
<img class="h-13" src="/image_slides/slides-2023-12-28-18-27-16.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>
</div>
<div class="text-left col-span-4">

* Kafka：2.8.1

### （Latest Release Version: 3.4.0）
###  * 扩展了Strimzi Kafka Operator
###  * 引入了Kafka集群管理界面
</div>
</div>

<div grid="~ cols-5 gap-4">
<div class="text-left">
<img class="h-13" src="/image_slides/slides-2023-12-28-18-27-55.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>
</div>
<div class="text-left col-span-4">

* HDFS：3.1.1

### （Latest Release Version: 3.3.4）
###  * 扩展了开源的Kubernetes HDFS项目
###  * 支持了persistent volumes以及虚机网络
</div>
</div>

<div grid="~ cols-5 gap-4">
<div class="text-left">
<img  class="h-10" src="/image_slides/slides-2023-12-28-18-31-29.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>
</div>
<div class="text-left col-span-4">

* MinIO：2022-09-07

### （Latest Release Version: 2023-02-27）
###  * 采用OpenEBS LocalPV来创建PV
</div>
</div>

<div grid="~ cols-5 gap-4">
<div class="text-left">
<img class="h-13" src="/image_slides/slides-2023-12-28-18-30-26.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>
</div>

<div class="text-left col-span-4">

* ClickHouse: 0.21.3

### （Latest Release Version: 1.16.1）
###  * 集成社区ClickHouse Operator
###  * 改造与Zookeeper集成流程
</div>
</div>

<div grid="~ cols-5 gap-4">
<div class="text-left">
<img class="h-13" src="/image_slides/slides-2023-12-28-18-29-22.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>
</div>

<div class="text-left col-span-4">

* Starrocks: 3.1.2

### （Latest Release Version: 1.16.1）
###  * 改造社区K8s Operator
###  * 与Hive Catalog集成
</div>
</div>

</div>

---
layout: items
---

## 15 多租户和安全管理

<div grid="~ cols-2 gap-4">
<div>

云原生的多租户管理

### 每个新用户都会创建单独的用户账号和对应的 Kerberos keytab，并加入相应的安全组。每个安全组都有自己独立的 K8s 命名空间，并独立发布计算作业，每个命名空间都有对应资源配额，实现多租户的用户管理和资源隔离。

云原生的安全管理

### 实现系统所有集成大数据组件的统一单点登录、Kerberos安全认证及Ranger授权管理。

</div>
<div>
<img class="h-75 mx-auto mt-5" src="/image_slides/slides-2023-11-02-10-41-48.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>
</div>
</div>

---
layout: intro
---

# 用户界面

User Interface

16 集群管理

17 应用管理

18 核心组件

19 租户管理

20 日志记录

21 监控告警

---
layout: items
---

## 16 集群管理

展示目标集群整体运行情况、集群节点、集群中各个组件安装运行情况、资源使用情况。支持对节点的隔离、排空、启动操作。

<img class="h-75 mx-auto shadow" src="/image_slides/slides-2023-11-02-15-54-25.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

---
layout: items
---

## 17 应用管理

对大数据组件以标准化配置文件的形式与统一系统服务对接，形成标准化部署，运行和运维流程。支持对大数据组件一键安装、卸载操作。支持对应用实例更新、停止、启动、卸载等操作。支持对应用负载进行重启、扩缩容操作。支持对应用 Pod 进行重启。对组件细颗粒度进行资源使用情况展示。

<img class="h-75 mx-auto shadow" src="/image_slides/slides-2023-11-02-15-56-16.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

---
layout: items
---

## 18 核心组件

KDP集成主流大数据组件 HDFS、Hive、Kafka、Spark、Flink、MinIO，常用开发工具 Hue、Airbyte、AutoML、MLFlow、Superset，高级管理组件 Ranger、Keyclock、Kerberos等。从系统主页及应用主页，便捷查看应用安装情况、运行状态、资源使用情况。提供完善系统使用说明及应用运维指南协助用户进行使用及运维。

KDP 引入新的大数据组件时，只需要按照标准配置文件进行配置，在几个小时内就可以快速实现新的大数据组件部署到 K8s。

<img class="h-65 mx-auto shadow" src="/image_slides/slides-2023-11-02-16-05-45.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

---
layout: items
---

## 19 租户管理

通过大数据集成基座进行多租户管理。每个新用户都会创建单独的用户账号和对应的 Kerberos keytab，并加入安全组。每个安全组都有自己独立的 K8s 命名空间，每个命名空间都有对应资源配额，每个安全组的计算作业都会发布到各自的命名空间。从而实现了多租户的用户管理和资源隔离。

<img class="h-75 mx-auto shadow" src="/image_slides/slides-2023-11-02-16-07-50.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

---
layout: items
---

## 20 日志记录

大数据集成基座为每个大数据组件的 pod 都配置了一个 sidecar 容器，容器中运行 Promtail 代理程序。Promtail代理程序专为 Loki 而设计，它获取大数据组件容器的日志，将日志转换为流，然后通过 HTTP API 将流推送到
Loki。
除了统一日志查询界面，同时也提供自研的 logviewer 服务，通过接口的方式获取大数据组件的日志。操作记录页面展示应用、安全组、用户、配置信息等多种实例的用户操作记录。支持全局查看租户内所有的操作日志信息。

<img class="h-75 mx-auto shadow" src="/image_slides/slides-2023-11-02-16-09-04.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

---
layout: items
---

## 21 监控告警

实现了 Prometheus 和 Grafana 的容器化发布。通过大数据集成基座，实现了大数据组件部署发布流程与监控报警系统 Prometheus 和 Grafana 进行自动地对接。

<img  class="h-75 mx-auto shadow" src="/image_slides/slides-2023-11-02-16-11-02.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

---
layout: intro
---

# 应用场景

Application Scenarios

22 高效的集群部署和运维

23 提升IT架构资源效率

24 自助式数字化创新

25 传统技术的升级改造

26 实时数仓方案

27 往期案例

---
layout: items
---

## 22 高效的集群部署和运维

有的企业作为技术提供方要为多个内部或外部的机构进行大数据集群的部署和实施。采用KDP，可以大幅度提升实施项目的部署效率，降低项目实施运维人力和时间成本。

<img class="h-90 mx-auto" src="/image_slides/slides-2023-10-18-18-28-16.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

---
layout: items
---

## 23 提升IT架构资源效率

有的企业在生产环境中运行多种类型的数据应用、不同类型的存储引擎、实时和批处理的计算作业。
采用了KDP以后，企业可以利用作业混排、存算分离和精细化调度等平台特性来提升整体资源使用效率，降低IT架构的投入成本。

<img class="h-80 mx-auto" src="/image_slides/slides-2023-10-18-18-30-30.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

---
layout: items
---

## 24 自助式数字化创新

有的企业需要有多个大数据集群服务不同的业务部门，业务部门的数据科学家希望能自助式地尝试新的云原生人工智能机器学习工具。
企业可以通过KDP部署提升多平台管理效率，提供数据分析和人工智能开发工具的自助式发布，降低整体资源消耗的成本，加速数据价值的创造过程。

<img class="h-80 mx-auto" src="/image_slides/slides-2023-10-18-18-29-15.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

---
layout: items
---

## 25 传统技术的升级改造

传统大数据平台因为技术扩展迭代流程比较慢，不能及时解决运维中碰到的性能瓶颈，同时大数据组件之间软件包依赖很复杂，导致组件升级困难，新的组件集成耗时费力。传统大数据平台逐步迁移到云原生大数据平台后，可以显著提升运维效率，降低运维成本，解放技术团队的生产力。

<img class="h-80 mx-auto" src="/image_slides/slides-2023-10-18-18-31-23.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

---
layout: items
---

## 26 实时数仓方案

<div grid="~ cols-2 gap-4">

<div class="text-left col-span-1">

技术选型

* K8s大数据平台 KDP，云原生的分布式技术架构，支持动态弹性扩容，支持高并发资源调度
* 分布式实时消息队列 Kafka，对接虚拟智能网关，支持亿级秒级流式数据接入
* 分布式流处理框架 Flink，支持对有界和无界数据流进行分布式实时处理
* 内存数据库 Redis，支持秒级实时数据存储与查询
* 列式数据库 Clickhouse，支持高并发、OLAP分析场景
* 实时数仓引擎 Starrocks，支持秒级随机查询
* 分布式文件系统 Hdfs/对象存储系统 Minio

</div>

<div class="text-left col-span-1">

数仓架构

<br>

<img class="h-auto" src="/image_slides/stream_data_warehouse.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

</div>

</div>

---
layout: items
---

## 27 往期案例

<div grid="~ cols-2 gap-4">

<div class="text-left">

武汉市卫健委大数据平台
### * 基于KDP的大数据平台在武汉市卫健委安全可靠地支持了多次动态扩容和升级
### * 集群资源使用率一直保持60%以上，充分利用计算和存储资源
### * 系统可靠性和性能在多次全民核酸检测中得到充分验证

</div>

<div class="text-left">

第一高楼中国尊大数据平台
### * 北京第一高楼中国尊采用KDP大数据平台处理500万传感器实时和交互数据处理
### * 在统一集群中处理实时，流式，数仓数据，在远程运维的情况下基本无需人工干预

</div>

<div class="text-left">

某头部运营商Hadoop云化体系
### KDP在某头部运营商的落地，支撑业务应用，满足业务的连续性不间断运行。

</div>

<div class="text-left">

其它案例
### 蔚来汽车金融云原生数据平台，百丽鞋业集团云原生数据平台，湖北省发改委宏观经济大数据分析平台、国网湖南数据中台全链路监测、嘉德拍卖大数据平台

</div>

</div>

---
layout: intro
---

# 部署规划

Deployment and Maintenance

28 节点规划

29 其他配置

---
layout: items
---

## 28 节点规划

<div grid="~ cols-5">
<div class="col-span-3">
BootStrap节点（引导节点）

### BootStrap节点是云原生大数据平台的引导、管理的入口节点。在部署云原生大数据平台时该节点起到部署引导作用，通过该节点对集群中其它两类节点进行初始化配置部署；在平台使用时期，该节点起到了代理节点的作用（bdos-proxy），对整个集群的管理使用都可以通过该代理节点进行访问使用，同时该节点还为整个集群提供私有化进行仓库的服务（bdos-registry）。

Master节点（控制节点）

### Master节点是云原生大数据平台的控制大脑，是管理层面节点，负责管理所有Node节点，负责调度Pod在哪些Node节点运行，负责控制集群运行过程中的所有状态，负责进行各类应用Pod运行的调度和编排。

Node节点（工作节点）

### Node节点是云原生大数据平台的工作负载，是工作层面节点，为整个云原生大数据平台提供各自的计算资源（CPU资源、MEM资源）以及存储资源，负责管理云原生大数据平台上运行的大数据组件以及管理组件的所有容器（container）。
</div>

<div class="col-span-2  py-15">
<img class="h-70 mx-auto" src="/image_slides/slides-2023-11-02-16-34-29.png" style="background: white; padding: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);"/>

</div>
</div>

---
layout: items
---

## 29 其他配置

主机⽹络配置

* 集群任意主机需要分配固定的IPv4地址且后续不可变更。
* 集群任意主机之间的所有协议(ICMP/TCP/UDP)、端⼝访问没有限制。

主机磁盘挂载

* 集群主机创建时，根⽬录⽂件系统强烈推荐通过LVM⽅式挂载。
* 集群主机初始状态时，数据盘挂载到主机即可，⽆需格式化。

其他资源

* 集群主机出⽅向可访问公⽹NTP源，或内⽹提供的NTP源。
* 集群主机出⽅向可访问公⽹DNS服务器，或内⽹提供DNS服务器。

---
layout: cover
class: text-center
---

# 谢谢聆听
