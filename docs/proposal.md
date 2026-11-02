# Project Proposal: Team daunting-horizon

Daniel Baglini, Thomas Gould, Lasya Kadiyala, Hrishikesh Kayshap, Mita Somoyeeta

Our three ideas are ranked below. We'd most like to build the first one.

All three would use Rails or Django with PostgreSQL and server-rendered pages, and would call an LLM through OpenRouter.

## 1. McNay's Cookie Orderer

**Tagline:** Reserve a McNay's cookie between classes, with AI suggestions for what to order.

The line at McNay's between classes is long. If you can reserve a pickup window ahead of time, you can grab your order and get to your next class.

### User journeys
- As a Yale student, I sign up with my @yale.edu email and a password.
- I describe what I like in my own words ("not too sweet, nut-free, love chocolate").
- To order, I pick a pickup window that still has room, look at the suggested items and the menu, reserve what I want, and get a pickup code.
- Before pickup, I can see my window, my code, and where to meet. I can cancel before the cutoff.
- As an operator, I log in to the admin page, see orders grouped by window, open and close windows, and mark each order ready, picked up, no-show, or cancelled.

### MVP features
1. Accounts limited to @yale.edu email addresses.
2. Pickup windows with a start time, an order cutoff, and a capacity.
3. A small menu with availability per window, and reservations with pickup codes. Students pay in person at pickup.
4. An operator dashboard for windows and orders.
5. AI order suggestions.

**What we'd skip:** online payment, email verification, menu editing, delivery, loyalty rewards, group orders.

### AI feature
The LLM reads a student's preferences, their past orders, and what's available in the chosen window, then suggests two or three items with a short reason for each (for example, "Oatmeal raisin: not too sweet and nut-free"). We only show suggestions that match items actually on the menu for that window.

If we have time after the MVP, we'd add a demand estimate for each window based on past orders and class end times. The LLM would turn it into a short note the operator can send to the bakery, such as "Tuesday 11:35: expect about 40 chocolate chip, since two large SOM classes end at 11:30."

### Plan
- **Sprint 1 (Nov 11):** sign-up and login, pickup windows, deployed.
- **Sprint 2 (Nov 18):** menu, reservations, capacity and cutoff rules, pickup codes.
- **Sprint 3 (Dec 2):** operator dashboard, preferences, AI suggestions.
- **Sprint 4 (Dec 11):** demand estimate and bakery note, testing, polish.

## 2. Ticketless Parking Check-In

**Tagline:** Check in and out of a parking lot without a ticket. AI confirms it's your registered car.

### User journeys
- As a driver, I sign up, register my car (plate, make, color), and see what I owe for past visits.
- When I arrive, the entry kiosk takes a photo of my car and starts my session.
- When I leave, the exit kiosk takes another photo, ends my session, and shows how long I parked and what I owe.
- As the lot operator, I see which cars are in the lot, review flagged sessions, and set the hourly rate.

### MVP features
1. Driver accounts with registered cars.
2. A kiosk page that takes a webcam photo (or an uploaded photo) at entry and exit. If the plate can't be read, the driver can type it in.
3. Parking sessions with the fee calculated from time parked.
4. An operator dashboard with current cars, flagged sessions, and rates.

**What we'd skip:** gate hardware, card payments, dedicated plate-reader cameras, multiple lots, reservations.

### AI feature
A vision-capable LLM reads the plate and describes the car in each photo, and the app compares the result to the registered car. It flags sessions where something doesn't match, like the wrong make or color, an unregistered plate, or an exit with no entry. The operator makes the final call on each flag.

## 3. StageCraft

**Tagline:** Theater production management from script to stage.

### User journeys
- As a director, I create a production, paste in the script, split it into scenes, cast actors in roles, and see upcoming rehearsals and open tasks.
- As a director planning rehearsals, I schedule sessions, choose the scenes to work on, see who needs to be there, take attendance, and track which scenes need more work.
- As an actor, I see my role, my scenes and lines, my rehearsal schedule, and notes from the director.
- As a stage manager, I add lighting, sound, and set-change cues to script lines and print the cue sheet.

### MVP features
1. Productions with members and roles (director, actor, crew, stage manager).
2. The script stored by scene and line, with each character linked to their scenes.
3. A rehearsal scheduler with attendance tracking.
4. A tracker for props, costumes, set items, and tasks.
5. A cue sheet tied to script lines.

**What we'd skip:** messaging, video, live voice rehearsal, ticketing, light and sound board control, PDF script import, public show listings.

### AI feature
The LLM reads the script and drafts a breakdown: the characters, the scene breaks, who appears in each scene, the props, costumes, and set pieces needed, and suggested lighting and sound cues. The director reviews each item, fixes whatever is wrong, and saves the rest.

Later on, it could summarize rehearsal notes or act as a line partner, reading the other characters in a scene so an actor can practice alone.
