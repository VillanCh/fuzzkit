# Fuzzkit - 批量生成特定 Payload 的 Fuzz 版本的模板系统

## 功能：

* （lex）词法解析寻找边界，针对边界进行 Fuzz
* （render）针对指定模板标签进行渲染（随机值or定制随机）
* 支持多个参数的交叉渲染

##基本概念与定义

### 目的
在漏洞挖掘中经常会出现需要对某一个点（边界，或者其他点）进行 Fuzz 测试，或者你使用 Burpsuite 或者是凭经验总结自己的字典，进行手动测试，难免出现测试不全的问题（疏忽某些特殊字符或特殊编码形式），本工具的功能其实非常简单：

* 任何位置
* 任何随机（单次随机与每次随机都可以支持）
* 任何字符
* 任何编码

定制与自动生成原 Payload 的各种 Fuzz 版本测试 WAF 的健壮性。

### 模板标签定义：

模板变量标记（可配置）：

	\_S\_S
	\_E\_E

随机变量标记：

  NS
	N
	NC
	S
	C
	UUID

枚举变量标记：

	ENUM

普通变量标记：

  X

### 定义

* 模板变量：会被 Scalpel 识别并且参与渲染的值（被标记名标记）
* 模板标记：模板标记标记当前模板变量的用途
* 模板变量名：模板变量的名称（某些标记可以省略模板变量名，某些标记不可以，是外界区分这个模板标记的途径）

#### 模板变量开始  

* `_S_S` 开始模板变量值
* `_E_E` 结束模板变量值


#### 内置模板

##### 随机型变量标记：

随机型变量标记只被渲染器渲染一次，并且如果 tag 参数没有设置的话，则不反馈回渲染的值。  

* `NS(tag){length_min,length_max}` or `NS(tag){length}`
	* NS：代表数字组成的字符串，例如：12345，234，2341
	* tag【不可省略】：代表这个模板变量的具体名称
	* length_min【可省略】 与 length_max【可省略】 代表组成这个数字字符串的最小位数和最大位数，默认为8
	* tag 可省略 length_min 与 length_max 默认值都为 8，如果大括号只有一个数字,就是指定位数
	* length：默认值为8
	* Example：
		* 模板 `{[{NS(tagname){3,6}}]}` 传入参数被渲染为 000-999999 中的任意一个（如1234，1246，7463）
		* 模板 `{[{NS{3,6}}]}` 传入参数被渲染为 000-999999 中的任意一个（如134123...）
		* 模板 `{[{NS}]}` 传入参数被渲染为 00000000-99999999 中的任意一个（如43567235,...）

---

* `N(tag){min,max}`  
	* N：代表数字（有大小）
	* tag：模板变量具体名称（不可以省略）
	* min：这个数字的最小值为`min`
	* max：这个数字的最大值为`max`
	* Example：
		* 模板 `{[{N(numbername){3,6}}]}` 被渲染后符合要求的值为 `3，4，5，6` 会随机挑选一个值填入模板中
		* 模板 `{[{N{3,6}}]}` 被渲染后符合要求的值为 `3，4，5，6` 会随机挑选一个值填入模板中

---
* `NC(tag){length_min,length_max}` or `NC(tag){length}`
	* NC：代表数字与字母组成的字符串，例如：1a2c3d24a5，23ad4，2qer3k41l
	* tag【不可省略】：代表这个模板变量的具体名称
	* length_min【可省略】 与 length_max【可省略】 代表组成这个字符串的最小位数和最大位数，默认为8
	* tag 可省略 length_min 与 length_max 默认值都为 8，如果大括号只有一个数字,就是指定位数
	* length：默认值为8
	* Example：
		* 模板 `{[{NC(tagname){3,6}}]}` 传入参数被渲染为包涵数字和字母的字符串（如1gc4，1yv6，74atw3）
		* 模板 `{[{NC{3,6}}]}` 传入参数被渲染为长度为3到6位的字符串（无特殊符号）
		* 模板 `{[{NS}]}` 传入参数被渲染为 00000000-99999999 中的任意一个（如43567235,...）

---

* `S(tag){length_min,length_max}` or `S(tag){length}`
* `C(tag){length_min,length_max}` or `C(tag){length}`(注：S 与 C 的标记是相同的)
	* S/C：代表纯字符串
	* tag：表模板变量的变量名
	* length_min：最小长度
	* length_max：最大长度
	* length：指定长度 默认值为 8
	* Example：
		* 模板 `{[{S(tagname){4,6}}]}` 可以为渲染为 adsf, rtws, sfgyh, ertquc 这类字符串
		* 模板 `{[{S{4,6}}]}` 可以为渲染为 adsf, rtws, sfgyh, ertquc 这类字符串
		* 模板 `{[{S{4}}]}` 可以为渲染为 adsf, rtws 这类字符串
		* 模板 `{[{S}]}` 可以为渲染为 adsfrtws, sfertquc，adhcnsht 这类字符串

---

* `UUID(tag){param}`
	* UUID：生成一个 UUID 字符串
	* tag：为变量名称
	* param：值为 raw 或者 hex，对结果的影响在 Example 说明，当输入不识别的 param 时自动设置为 raw
	* Example：
		* `UUID{raw}` 渲染为 a0893c6e-c684-11e6-9ad4-c0335e0a1d78
		* `UUID(tag){raw}` 渲染为 a0893c6e-c684-11e6-9ad4-c0335e0a1d78
		* `UUID{hex}` 渲染为a0893c6ec68411e69ad4c0335e0a1d78
		* `UUID(tag){hex}` 渲染为a0893c6ec68411e69ad4c0335e0a1d78

---

##### 枚举型标记

枚举型变量标记必须注明该模板变量的名称，因为参数必须来源于外界参数（需要一个 generator 或者任何 iter 类型的变量）

* `ENUM(tag)`
	* ENUM：表明这个模板变量是要被多次渲染生成多个 Payload 的。
	* tag：表明这个模板变量的变量名：传入参数必须是可以迭代的对象

##### 普通标记

普通型变量标记必须注明模板变量的名称，因为参数必须来源于外界参数（参数是一个可以 repr 的值）

* `X(tag)`
	* X：表明这个模板变量是指定用户输入的
	* tag：模板变量名称

## 基础用法 Quick Start

要素 ：

1. 一个已知的 Payload 模板  
2. 模板需要渲染的位置标记
3. （Option）标记位置需要渲染的值

示例：  
模板`{[{X(border)}]}<scr{[{ENUM(xxx)}]}ipt{[{N(asdf){444,997}}]}></scr{[{ENUM(enumt)}]}ip{[{ENUM(enumts)}]}t>`

        scalpel = Scalpel(template='{[{X(border)}]}<scr{[{ENUM(xxx)}]}ipt{[{N(asdf){444,997}}]}></scr{[{ENUM(enumt)}]}ip{[{ENUM(enumts)}]}t>',
                          enumt=['1','2','5','6'],
                          enumts=['7','a','c','6'],
                          xxx=['c','e3','adf','xss'],
                          border='Fuckin')
        for i in scalpel.payloads:
            print i

运行结果：

	Fuckin<scrcipt704></scr1ip7t>
	Fuckin<scrcipt548></scr1ipat>
	Fuckin<scrcipt641></scr1ipct>
	Fuckin<scrcipt762></scr1ip6t>
	Fuckin<scre3ipt980></scr1ip7t>
	Fuckin<scre3ipt960></scr1ipat>
	Fuckin<scre3ipt913></scr1ipct>
	Fuckin<scre3ipt524></scr1ip6t>
	Fuckin<scradfipt549></scr1ip7t>
	Fuckin<scradfipt871></scr1ipat>
	Fuckin<scradfipt507></scr1ipct>
	Fuckin<scradfipt496></scr1ip6t>
	Fuckin<scrxssipt679></scr1ip7t>
	Fuckin<scrxssipt555></scr1ipat>
	Fuckin<scrxssipt541></scr1ipct>
	Fuckin<scrxssipt524></scr1ip6t>
	...
	...
	...
	Fuckin<scradfipt952></scr6ipct>
	Fuckin<scradfipt871></scr6ip6t>
	Fuckin<scrxssipt447></scr6ip7t>
	Fuckin<scrxssipt982></scr6ipat>
	Fuckin<scrxssipt887></scr6ipct>
	Fuckin<scrxssipt771></scr6ip6t>

根据观察：

* X 标记处被替换成指定值
* N 标记处被替换成指定大小区间的数字
* ENUM 标记处被生成多个 Payload 遍历出来
* 多个 ENUM 的时候，所有的组合都会被生成

## 拓展
### TODO LIST：

1. 提供内置 FUZZ 数据库
2. 更高级的标签系统封装让模板看起来不太臃肿
3. 针对 WEB 的边界分析
