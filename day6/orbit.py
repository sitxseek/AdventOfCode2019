orbits = [line.rstrip() for line in open('input.txt')]

orbit_num = {}
orbit_map = {}
orbiter_to_orbitee = {}

# part 1
def update_children(child):
    for c in orbit_map.get(child, []):
        orbit_num[c] = orbit_num[child] + 1
        update_children(c)

for orbit in orbits:
    orbitee = orbit.split(")")[0]
    orbiter = orbit.split(")")[1]
    orbiter_to_orbitee[orbiter] = orbitee
    existing = orbit_map.get(orbitee, [])
    existing.append(orbiter)
    orbit_map[orbitee] = existing
    orbit_num[orbiter] = orbit_num.get(orbitee, 0) + 1
    update_children(orbiter)
    
# part 2
curr_orbitee = "YOU"
while True:
    orbit_map[curr_orbitee] = ["YOU"]
    if curr_orbitee == "COM":
        break
    else:
        curr_orbitee = orbiter_to_orbitee[curr_orbitee]

transfers = 0
lca = orbiter_to_orbitee["SAN"]
while "YOU" not in orbit_map[lca]:
    transfers += 1
    lca = orbiter_to_orbitee[lca]

curr_orbiter = "YOU"
while orbiter_to_orbitee[curr_orbiter] != lca:
    transfers += 1
    curr_orbiter = orbiter_to_orbitee[curr_orbiter]

print(sum(orbit_num.values()))
print("Transfers:", transfers)