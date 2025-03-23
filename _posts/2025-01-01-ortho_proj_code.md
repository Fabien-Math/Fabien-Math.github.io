---
layout: post
title: Orthogonal projection
date: 2025-01-01 00:00:00
description: Code for orthogonal projection between a point and a line
tags: formatting code
categories: 
tabs: true
---

## Orthogonal projection
This post provides code examples in Python and C++ demonstrating how to compute the shortest distance between a point and a line using orthogonal projection mathematical principles. The implementation uses the formula $$\displaystyle \frac{|ax + by - c|}{\sqrt{a^2 + b^2}}$$ where the line is represented as $$ax + by = c$$.

{% tabs log %}

{% tab log Python %}

```python
def orthogonal_projection(p:tuple, line:tuple) -> float:
	"""Compute the shortest distance between a point and a line ax + by = c"""
	a, b, c = line
	return abs(a*p[0] + b*p[1] - c)/sqrt(a**2 + b**2)
```

{% endtab %}

{% tab log C++ %}

```cpp
double orthogonal_projection(const std::pair<double, double>& p, const std::tuple<double, double, double>& line) {
	// Compute the shortest distance between a point and a line ax + by = c
	double a = std::get<0>(line);
	double b = std::get<1>(line);
	double c = std::get<2>(line);
	return std::abs(a*p.first + b*p.second - c)/std::sqrt(a*a + b*b);
}
```

{% endtab %}

{% endtabs %}
