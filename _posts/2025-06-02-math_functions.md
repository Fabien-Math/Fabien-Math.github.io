---
layout: post
title: Useful math functions
date: 2025-06-02 00:00:00
description: Mathematical function utility in Python
tags: math
categories: 
tabs: true
---


## Lines

### Line equation

{% tabs log %}

{% tab log Python %}

```python
def compute_line(p1:tuple, p2:tuple):
	"""Compute line equation : ax + by = c"""
	a = p2[1] - p1[1]
	b = p1[0] - p2[0]
	c = p1[0] * (p2[1] - p1[1]) - p1[1] * (p2[0] - p1[0])
	return a,b,c
```

{% endtab %}

{% tab log C++ %}

```cpp
// To be done
```

{% endtab %}

{% endtabs %}

### Line evaluation
{% tabs log %}

{% tab log Python %}

```python
def evaluate_line(l:tuple, x:float) -> float:
	"""Evaluate the line in 'x'

	Args:
		l (tuple): (a, b, c) for ax + by = c
		x (float): x to be evaluated

	Returns:
		float: line value in x
	"""
	if l[1] != 0:
		return (l[2] - l[0] * x) / l[1]
	else:
		return x
```

{% endtab %}

{% tab log C++ %}

```cpp
// To be done
```

{% endtab %}

{% endtabs %}


## Itersections

### Lines intersections
{% tabs log %}

{% tab log Python %}

```python
def compute_line_inter(l1:tuple, l2:tuple) -> tuple|bool:
	"""Find the intersection point between two lines if it exists (ax + by = c)"""
	a1, b1, c1 = l1
	a2, b2, c2 = l2
	d = a1*b2 - a2*b1
	if d:
		x = (c1*b2 - c2*b1)/d
		y = (a1*c2 - a2*c1)/d
		return x, y
	return False
```

{% endtab %}

{% tab log C++ %}

```cpp
// To be done
```

{% endtab %}

{% endtabs %}


### Segments intersection
{% tabs log %}

{% tab log Python %}

```python
def compute_segment_inter(p11:tuple, p12:tuple, p21:tuple, p22:tuple) -> tuple|bool:
	"""Find the intersection point between two segment if it exists"""
	l1 = compute_line(p11, p12)
	l2 = compute_line(p21, p22)
	p_inter = compute_line_inter(l1, l2)
	if p_inter:
		if point_in_box(p_inter, p11, p12):
			if point_in_box(p_inter, p21, p22):
				return p_inter
	return False```

{% endtab %}

{% tab log C++ %}

```cpp
// To be done
```

{% endtab %}

{% endtabs %}



### Circles intersections
{% tabs log %}

{% tab log Python %}

```python
def compute_circle_inter(p1:tuple, r1:float, p2:tuple, r2:float) -> tuple|None:
	"""Find the intersection point between two circle if it exists"""
	d = distance(p1, p2)
	if d >= (r1 + r2):
		print("No circle intersection found (d >= (r1 + r2)) ! Returned None")
		return None
	if d <= abs(r1 - r2):
		print("No circle intersection found (d < abs(r1 - r2)) ! Returned None")
		return None
	if d < 1e-6 and abs(r1 - r2) < 1e-6:
		print("No circle intersection found (abs(r1 - r2) < 1e-6) ! Returned None")
		return None
	
	# https://lucidar.me/fr/mathematics/how-to-calculate-the-intersection-points-of-two-circles/
	a = (r1**2 - r2**2 + d**2)/(2*d)
	# print(p1, r1, p2, r2, d, a)
	h = sqrt(r1**2 - a**2)

	x5 = p1[0] + (a / d) * (p2[0] - p1[0]) 
	y5 = p1[1] + (a / d) * (p2[1] - p1[1]) 

	xi1 = x5 - h * (p2[1] - p1[1])/d
	yi1 = y5 + h * (p2[0] - p1[0])/d

	xi2 = x5 + h * (p2[1] - p1[1])/d
	yi2 = y5 - h * (p2[0] - p1[0])/d

	pi1 = (xi1, yi1)
	pi2 = (xi2, yi2)
	return pi1, pi2
```

{% endtab %}

{% tab log C++ %}

```cpp
// To be done
```

{% endtab %}

{% endtabs %}


### Segment - rectangle intersection

{% tabs log %}

{% tab log Python %}

```python
def compute_segment_rect_inter(line:tuple, line_p1:tuple, line_p2:tuple, rect:list) -> tuple|bool:
	"""Compute the intersection between two segment

	Args:
		line (tuple): Line
		line_p1 (tuple): First point of the segment defined by the line
		line_p2 (tuple): Second point of the segment defined by the line
		rect (list): List of point of a rect (x1, y1, x2, y2)

	Returns:
		bool: If the two segment collide
	"""
	# rect = (x1, y1, x2, y2) avec p1 top-left et p2 bottom-right 
	points = [(rect[0], rect[1], rect[0], rect[3]),
				(rect[0], rect[3], rect[2], rect[3]),
				(rect[2], rect[3], rect[2], rect[1]),
				(rect[2], rect[1], rect[0], rect[1])]
	for p1x, p1y, p2x, p2y in points:
		p1 =(p1x, p1y)
		p2 =(p2x, p2y)

		line_rect = compute_line(p1, p2)
		intersection = compute_line_inter(line, line_rect)

		if intersection is not False:
			if point_in_box(intersection, p1, p2):
				if point_in_box(intersection, line_p1, line_p2):
					return intersection
	
	return False
```

{% endtab %}

{% tab log C++ %}

```cpp
// To be done
```

{% endtab %}

{% endtabs %}


## Point in shapes


### Point in box
{% tabs log %}

{% tab log Python %}

```python
def point_in_box(p:tuple, p1:tuple, p2:tuple, error_offset:float = 1e-6) -> bool:
	"""Check if the point 'p' is in the box defined by p1 and p2

	Args:
		p (tuple): Point to be checked
		p1 (tuple): First point
		p2 (tuple): Second point
		error_offset (float, optional): Error offset to overcome python binary error on float. Defaults to 1e-6.

	Returns:
		bool: If the point is in the box
	"""
	if p[0] > min(p1[0], p2[0]) - error_offset and p[0] < max(p2[0], p1[0]) + error_offset:
		if p[1] > min(p1[1], p2[1]) - error_offset and p[1] < max(p2[1], p1[1]) + error_offset:
			return True
	return False
```

{% endtab %}

{% tab log C++ %}

```cpp
// To be done
```

{% endtab %}

{% endtabs %}

### Point in circle
{% tabs log %}

{% tab log Python %}

```python
def point_in_circle(p:tuple, center:tuple, radius:float) -> bool:
	"""Check if the point is in the circle"""
	if distance(p, center) <= radius:
		return True
	return False
```

{% endtab %}

{% tab log C++ %}

```cpp
// To be done
```

{% endtab %}

{% endtabs %}


### Point in polygon
{% tabs log %}

{% tab log Python %}

```python
def point_in_polygon(point:tuple, polygon:list[tuple]) -> bool:
	"""Check if the point is in the polygon

	Args:
		point (tuple): Point to be checked
		polygon (list): List of point defining the polygon
	"""
	x, y = point
	n = len(polygon)
	inside = False
	p1x, p1y = polygon[0]
	for i in range(1, n + 1):
		p2x, p2y = polygon[i % n]
		if y > min(p1y, p2y):
			if y <= max(p1y, p2y):
				if x <= max(p1x, p2x):
					if p1y != p2y:
						xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
					if p1x == p2x or x <= xinters:
						inside = not inside
		p1x, p1y = p2x, p2y
	return inside
```

{% endtab %}

{% tab log C++ %}

```cpp
// To be done
```

{% endtab %}

{% endtabs %}



## Tab example

### Title
{% tabs log %}

{% tab log Python %}

```python
# To be done
```

{% endtab %}

{% tab log C++ %}

```cpp
// To be done
```

{% endtab %}

{% endtabs %}