## challenge diff

```diff
27,35d26
< def is_hori_or_vert(coord: list) -> bool:
< 	"""
< 		Check if a coordinate pair is a horizontal or vertical line
< 	"""
<
< 	(x1, y1), (x2, y2) = coord
<
< 	return (x1 == x2) or (y1 == y2)
<
50c41
< 	if y1 == y2:
---
> 	elif y1 == y2:
51a43,45
>
> 	else:
> 		for x, y in zip(r(x1, x2), r(y1, y2)): grid[x][y] += 1
71,74c65
< 	for ev in hydro_vents:
< 		if not is_hori_or_vert(ev): continue
< 		mark_line(ev)
<
---
> 	for ev in hydro_vents: mark_line(ev)
```
