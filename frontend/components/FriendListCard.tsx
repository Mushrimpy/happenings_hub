import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/components/ui/card"
import { Avatar, AvatarImage, AvatarFallback } from "@/components/ui/avatar"
import { Button } from "@/components/ui/button"

export function FriendListCard() {
    return (
        <div className="w-full h-full p-8 bg-gray-100 dark:bg-gray-800">
            <div className="grid gap-10 px-40">
                <Card className="w-full">
                    <CardHeader className="flex flex-row items-start">
                        <div className="space-y-1.5">
                            <CardTitle>Friend Requests</CardTitle>
                            <CardDescription>You have 5 pending requests.</CardDescription>
                        </div>
                    </CardHeader>
                    <CardContent className="border-t pt-4">
                        <div className="space-y-4">
                            <div className="flex items-center justify-between">
                                <Avatar className="h-9 w-9">
                                    <AvatarImage src="/placeholder-user.jpg" alt="User" />
                                    <AvatarFallback>JP</AvatarFallback>
                                </Avatar>
                                <div className="ml-4">
                                    <p className="text-sm font-medium">John Doe</p>
                                    <p className="text-sm text-gray-500 dark:text-gray-400">john.doe@example.com</p>
                                </div>
                                <div className="ml-auto">
                                    <Button variant="outline" className="mr-2">
                                        Decline
                                    </Button>
                                    <Button>Accept</Button>
                                </div>
                            </div>
                        </div>
                    </CardContent>
                    <CardFooter>
                        <Button variant="link" className="ml-auto">
                            View All
                        </Button>
                    </CardFooter>
                </Card>
                <Card className="w-full">
                    <CardHeader className="flex flex-row items-start">
                        <div className="space-y-1.5">
                            <CardTitle>Friends</CardTitle>
                            <CardDescription>You have 10 friends.</CardDescription>
                        </div>
                    </CardHeader>
                    <CardContent className="border-t pt-4">
                        <div className="space-y-4">
                            <div className="flex items-center justify-between">
                                <Avatar className="h-9 w-9">
                                    <AvatarImage src="/placeholder-user.jpg" alt="Friend" />
                                    <AvatarFallback>MA</AvatarFallback>
                                </Avatar>
                                <div className="ml-4">
                                    <p className="text-sm font-medium">Mary Anne</p>
                                    <p className="text-sm text-gray-500 dark:text-gray-400">mary.anne@example.com</p>
                                </div>
                                <div className="ml-auto">
                                    <Button variant="outline">Unfriend</Button>
                                </div>
                            </div>
                        </div>
                    </CardContent>
                    <CardFooter>
                        <Button variant="link" className="ml-auto">
                            View All
                        </Button>
                    </CardFooter>
                </Card>
            </div>
        </div>
    )
}