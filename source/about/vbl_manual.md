# Lab

This is the public lab book for the Virtual Brain Lab. We are part of the Steinmetz Lab at University of Washington. As a member of the VBL you can modify this document by making commits or pull requests directly to the [vbl-docs](https://github.com/VirtualBrainLab/vbl-docs) repository. Discussions about content can be done in the [issues](https://github.com/VirtualBrainLab/vbl-docs/issues).

## Values

The Virtual Brain Lab's goal is to make neuroscience *more accessible*, by developing *open-source* research tools that *benefit researchers and the public*.

#### Accessibility

Medical and biological science has historically benefited a small group of people. Science *continues* to marginalize women and people of color, as well as the public. One of the ways in which this happens is by making experimental tools and knowledge inaccessible to people who haven't had the right experiences or training. Our goal is to develop tools that make neuroscience available to all.  

#### Open-source & public benefit

It is our responsibility to ensure that the tools we build can be reused and built upon by future researchers. This is more than just a responsibility to share our code -- it's the responsibility to make sure we are building tools that are robust.

### Rules

 1. **Health and happiness, then work**. If you are unwell or exhausted, please don't work!
 2. **Build for the future**. Document your code, for your future self and your colleagues. 

### Guidelines

 1. **Work together**. Our group has diverse expertise and we are a collaborative environment, be intentional about relying on each other as resources.
 2. **Plan ahead**. Draw pictures, make diagrams on a whiteboard, talk about your plans. Don't write code until you have a vision for your infrastructure!
 3. **Take breaks**. Often, the solution to a problem will come to you when you step away from your work. Take time to nap, go on walks, and eat lunch with your coworkers.
 4. **Resolve conflicts when they start**. Part of working together is resolving conflicts. Try starting with: "I noticed X, it's effect on me is Y, how can we work on that?".
 5. **Take your ideas seriously**. Nobody knows your project as well as you do, any advice or feedback you get from colleagues is just that. You choose what to do with it.  
 6. **Be on time**. Meetings are expensive, both in time and money, and because they disrupt the ability to focus without interruptions. We minimize them to reduce that impact, but they can only be efficient if everybody works together to start and end them on time. 
 7. **If you're overwhelmed, that's okay**. Everybody's priorities shift over time. If you realize you're doing too much and need to cut back in one area, communicate that. 
 8. **Work at home, but don't bring your work home**. Dan's goal is to work 3 days a week in the lab, because in-person meetings are generally more effective and efficient than remote meetings. It's recommended you use a similar structure, but be careful when working remotely not to let your work encroach on your life. 

## Join the VBL

Are you motivated by the idea of building software for scientists? We are making interactive 3D visualization possible for research. In practice, that means working with large-scale datasets and doing data wrangling as well as building user-facing tools, often with the Unity game engine. 

Contact Dan Birman with inquiries/questions (dbirman@uw.edu).

### Undergraduate research at UW

Joining the VBL as a student is an opportunity to build applied technology while developing your skills as a programmer. As a member of a cutting-edge neuroscience laboratory at UW you will also learn a lot of neuroscience along the way. We pay all undergraduate researchers who join the VBL. Beacuse of this, there are limited spaces available.

### Software devs / Researchers

The VBL does not have independent funding to pay researchers (graduate students, postdocs, or software engineers). If you have your own funding or you are interested in working together to apply for funding please get in touch.

## Mentoring

All members of the VBL are responsible for ensuring the lab is a healthy environment for building cool things, challenging ourselves, and growing as researchers and developers.

Every member of the lab is expected to complete an individual development plan twice a year (every quarter for undergraduates). The IDP is a structured feedback process, designed to help identify both the achievements and challenges of the last year/quarter. The process has four steps: first, a self-reflection where you look back on your past goals and achievements and plan for the next period, second, a mentor-reflection where you receive external perspective as written comments, third, a one-on-one conversation about the whole document, and finally, a brief summary that you make to the lab. Both private and public IDP files are stored in Github repositories on the lab account. 

## Group Meeting

We attend the Steinmetz Lab meeting, see the wiki for details. Everybody is encouraged to attend, schedule permitting.

## Project organization

As a member of the VBL you will have at least one project that you are responsible for. Your project may be independent or a component in a much larger project.

If you are working on a single project, expect to spend about 75% of your time working independently and pair coding. 20% of your time will go to hackathons. Try to keep meetings to less than 10% and ideally less than 5% of your time. If you have a mentee, expect to shift 10% of your project time into the meeting category for each person you work with. Nobody in the lab should have more than five people who meet with them each week. 

### Software

Our main job is to develop software. Usually, these will be interactive 3D experiences for neuroscience data exploration. We primarily build in Unity, because it handles 3D interactions for us and simplifies the deployment process. We also often write code in Python and Javascript. All our code is shared open-source on [the lab github page](https://github.com/VirtualBrainLab/). 

### Collaboration

Each week you should expect to meet with your colleagues on your project to provide an update on progress and to do pair coding. You can keep the update portion short and efficient by writing down an agenda in advance. You should also plan to have some amount of pair coding time, where you show your colleagues what you built in the last week and learn about their systems. This is particularly important when someone adds a new framework. 

In addition to these in-person meetings, we use these documentation pages, email, Slack, and Github to communicate. In rough order from best to least preferred:

 * **Documentation**: public-facing explanations of features, including instructions for developers
 * **In-person/zoom**: for short private meetings and pair coding
 * **Github issues**: for to-do items. Use Projects to create filtered personal to-do lists
 * **Email**: for long-form private discussions where people need more time to think through their plans
 * **Slack**: use with caution, make sure to set your away hours and keep most channels muted. Always make replies in threads

It's easiest to always reach for Slack, but it's rarely the right way to communicate about something. Slack is hard to search and most conversations are private; once a thread gets dropped you may struggle to find it again later. 

### Documentation

If our tools aren't understandable, they aren't useful. If they can't be developed in the future, they aren't useful. Although we write papers to make our work citable and easily shareable, the documentation is the primary way we expect users to learn about and interact with our tools. For any public API, you are expected to document the code and add it to the API references. For any public tool, you are expected to make both written and video tutorials for any tool that you deploy. There is an art to building good tutorials, expect to iterate many times! For videos, you can use [OBS](https://obsproject.com/) to record your screen as you narrate.

#### Code style 

Documentation does not replace good coding style. Your classes, variables, and functions should be named so that they are easily understandable and they should be written so that they do what they say they do. If a line of code can't be understood even in context, it should have a comment explaining its purpose.

| Language | Classes | Public vars | Private vars | Functions | Function params / vars |
| --- | --- | --- | --- | --- | --- |
| C# | PascalCase | PascalCase | _camelCase | PascalCase | camelCase |
| Python | PascalCase | snake_case | snake_case | snake_case | snake_case |

 * **Static variables**: should start with the prefix `s_` 
 * **Constants**: SCREAMING_SNAKE_CASE

#### Best practices

To make our code easily understandable we follow a few best practices in Unity development. We use **static instances**, **UnityEvents**, and a three-level **code hierarchy**. Best to get an in-person tutorial on these concepts. 

### Deployment

We deploy all of our tools to Windows desktop and WebGL, at a minimum. It's not hard to deploy to linux as well, MacOS is more complicated. Use [semantic versioning](https://semver.org/) to track releases. Releases are permanent. In addition, keep in mind that we have a responsibility to maintain released code. Once you release a v1.0.0 release, you are expected to maintain backward compatibility in future releases until you move to the next major version. 

### Papers

We expect most users to engage with the software tools themselves and their documentation. Unfortunately, to have a career in academia, the primary currency remains *papers* and *citations*, not products. If you do a good job with your documentation, producing a paper from your project is just a matter of re-packaging the content with more context.

## Hackathons

To keep our momentum and excitement about projects, we have to be intentional about exploring new ideas and playing around with future possible tools. This shouldn't be something we do in our free time, this is a substantial part of our job! With this in mind, Dan asks that everybody set aside one week out of every five specifically to test *new* ideas. During hackathon weeks, everybody will work together on a test project **instead of** their main projects. Because everybody spends different amounts of time in the lab, each person's individual contribution to the hackathon will vary greatly. Work with your mentor to find a slice of the project that is appropriate to your skill and time and that you can finish within your work hours. Take advantage of hackathon weeks to stretch your skills. 

## Funding

Dan is happy to discuss the details of any of these grant applications with you at any time! Information about lab member grant applications is shared here with permission. You can access the final versions of any of these grants in the [lab drive](https://drive.google.com/drive/folders/1vhVtWFO8eRpVMmR5u4isGsgOycdBCEiK?usp=share_link). 

| Source    | Person  | Date applied  | Outcome   | Funding   |
| ---       | ---     | ---           | ---       | ---       |
| Heroku Open Source Credit Program | DB  | 2023 | Funded | $480 |
| UW Mary Gates Scholarship Resubmission | KY  | 2023 | Funded | $5,000 |
| NIH K99 Transition to Independence | DB | 2023 | Pending |  |
| Neurohub fellowship | DB | 2023 | Pending |  |
| UW Mary Gates Scholarship | KY  | 2022 | Not funded |  |
| WRF Galas Award | DB | 2022 | Not funded |  |
| NIH UE5-METER | DB | 2021 | Not funded |  |
| UW Mary Gates Scholarship | KN  | 2021 | Funded | $5,000 |
| UW CLIME Grant | DB | 2021 | Not funded |  |
| WRF Postdoctoral Fellowship | DB | 2019 | Funded | $280,000 |

## Sources

This document was inspired by the CLEAR lab manual and some of the excellent rules/guidelines are identical here. CLEAR. (2021). *CLEAR Lab Book: A living manual of our values, guidelines, and protocols*, V.03. St. John’s, NL: Civic Laboratory for Environmental Action Research, Memorial University of Newfoundland and Labrador.