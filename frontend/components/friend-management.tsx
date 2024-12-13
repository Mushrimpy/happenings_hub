'use client'

import { useState } from 'react'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { UserPlus, X, Check } from "lucide-react"

// Mock data
const mockFollowing = Array.from({ length: 50 }, (_, i) => ({
  id: i + 1,
  name: `Following User ${i + 1}`,
  username: `following_user_${i + 1}`,
  isFollowing: true,
}))

const mockFollowers = Array.from({ length: 50 }, (_, i) => ({
  id: i + 1,
  name: `Follower User ${i + 1}`,
  username: `follower_user_${i + 1}`,
  isFollowing: Math.random() > 0.5,
}))

const mockRequests = Array.from({ length: 5 }, (_, i) => ({
  id: i + 1,
  name: `Request User ${i + 1}`,
  username: `request_user_${i + 1}`,
}))

export function ConnectionsCard() {
  const [following, setFollowing] = useState(mockFollowing)
  const [followers, setFollowers] = useState(mockFollowers)
  const [requests, setRequests] = useState(mockRequests)
  const [newFollowUsername, setNewFollowUsername] = useState('')
  const [currentPage, setCurrentPage] = useState({ following: 1, followers: 1 })
  const itemsPerPage = 10

  const handleFollow = (e: React.FormEvent) => {
    e.preventDefault()
    // In a real app, you would make an API call here
    const newFollow = {
      id: following.length + 1,
      name: `User ${following.length + 1}`,
      username: newFollowUsername,
      isFollowing: true,
    }
    setFollowing([newFollow, ...following])
    setNewFollowUsername('')
  }

  const toggleFollow = (id: number, list: 'following' | 'followers') => {
    const updateList = list === 'following' ? following : followers
    const updatedList = updateList.map(user =>
      user.id === id ? { ...user, isFollowing: !user.isFollowing } : user
    )
    list === 'following' ? setFollowing(updatedList) : setFollowers(updatedList)
  }

  const handleRequest = (id: number, action: 'confirm' | 'delete') => {
    if (action === 'confirm') {
      const confirmedUser = requests.find(req => req.id === id)
      if (confirmedUser) {
        setFollowers([{ ...confirmedUser, isFollowing: false }, ...followers])
      }
    }
    setRequests(requests.filter(req => req.id !== id))
  }

  const removeFollower = (id: number) => {
    setFollowers(followers.filter(follower => follower.id !== id))
  }

  const paginatedList = (list: typeof following, page: number) =>
    list.slice((page - 1) * itemsPerPage, page * itemsPerPage)

  const Pagination = ({ list, currentPage, setCurrentPage }: {
    list: 'following' | 'followers',
    currentPage: number,
    setCurrentPage: (page: number) => void
  }) => (
    <div className="flex justify-center mt-4 space-x-2">
      <Button
        variant="outline"
        onClick={() => setCurrentPage(currentPage - 1)}
        disabled={currentPage === 1}
      >
        Previous
      </Button>
      <Button
        variant="outline"
        onClick={() => setCurrentPage(currentPage + 1)}
        disabled={currentPage * itemsPerPage >= (list === 'following' ? following.length : followers.length)}
      >
        Next
      </Button>
    </div>
  )

  return (
    <div className="container mx-auto px-8 py-6 max-w-4xl">

      <Tabs defaultValue="following">
        <TabsList className="grid w-full grid-cols-2">
          <TabsTrigger value="following">Following</TabsTrigger>
          <TabsTrigger value="followers">Followers</TabsTrigger>
        </TabsList>

        <TabsContent value="following" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle>Send Follow Request</CardTitle>
            </CardHeader>
            <CardContent>
              <form onSubmit={handleFollow} className="flex space-x-2">
                <Input
                  type="text"
                  placeholder="Enter username to follow"
                  value={newFollowUsername}
                  onChange={(e) => setNewFollowUsername(e.target.value)}
                  className="flex-grow"
                />
                <Button type="submit" className='bg-orange-600'>
                  <UserPlus className="mr-2 h-4 w-4" />
                  Follow
                </Button>
              </form>
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>Following</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <ul className="space-y-4">
                {paginatedList(following, currentPage.following).map((user) => (
                  <li key={user.id} className="flex items-center justify-between">
                    <div className="flex items-center space-x-4">
                      <Avatar>
                        <AvatarImage src={`https://api.dicebear.com/6.x/initials/svg?seed=${user.name}`} alt={user.name} />
                        <AvatarFallback>{user.name.split(' ').map(n => n[0]).join('')}</AvatarFallback>
                      </Avatar>
                      <div>
                        <p className="font-medium">{user.name}</p>
                        <p className="text-sm text-gray-500">@{user.username}</p>
                      </div>
                    </div>
                    <Button
                      variant={user.isFollowing ? "secondary" : "default"}
                      onClick={() => toggleFollow(user.id, 'following')}
                    >
                      {user.isFollowing ? 'Following' : 'Follow'}
                    </Button>
                  </li>
                ))}
              </ul>
              <Pagination
                list="following"
                currentPage={currentPage.following}
                setCurrentPage={(page) => setCurrentPage({ ...currentPage, following: page })}
              />
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="followers" className="space-y-6">
          {requests.length > 0 && (
            <Card>
              <CardHeader>
                <CardTitle>Incoming Requests</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <ul className="space-y-4 mb-6">
                  {requests.map((request) => (
                    <li key={request.id} className="flex items-center justify-between">
                      <div className="flex items-center space-x-4">
                        <Avatar>
                          <AvatarImage src={`https://api.dicebear.com/6.x/initials/svg?seed=${request.name}`} alt={request.name} />
                          <AvatarFallback>{request.name.split(' ').map(n => n[0]).join('')}</AvatarFallback>
                        </Avatar>
                        <div>
                          <p className="font-medium">{request.name}</p>
                          <p className="text-sm text-gray-500">@{request.username}</p>
                        </div>
                      </div>
                      <div className="space-x-2">
                        <Button variant="ghost" size="sm" onClick={() => handleRequest(request.id, 'confirm')}>
                          <Check className="h-4 w-4" />
                        </Button>
                        <Button variant="ghost" size="sm" onClick={() => handleRequest(request.id, 'delete')}>
                          <X className="h-4 w-4" />
                        </Button>
                      </div>
                    </li>
                  ))}
                </ul>
              </CardContent>
            </Card>
          )}

          <Card>
            <CardHeader>
              <CardTitle>Followers</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <ul className="space-y-4">
                {paginatedList(followers, currentPage.followers).map((follower) => (
                  <li key={follower.id} className="flex items-center justify-between space-x-4">
                    <div className="flex items-center space-x-4">
                      <Avatar>
                        <AvatarImage src={`https://api.dicebear.com/6.x/initials/svg?seed=${follower.name}`} alt={follower.name} />
                        <AvatarFallback>{follower.name.split(' ').map(n => n[0]).join('')}</AvatarFallback>
                      </Avatar>
                      <div>
                        <p className="font-medium">{follower.name}</p>
                        <p className="text-sm text-gray-500">@{follower.username}</p>
                      </div>
                    </div>
                    <div className="space-x-2">
                      <Button
                        variant={follower.isFollowing ? "secondary" : "default"}
                        onClick={() => toggleFollow(follower.id, 'followers')}
                      >
                        {follower.isFollowing ? 'Following' : 'Follow'}
                      </Button>
                      <Button variant="ghost" size="sm" onClick={() => removeFollower(follower.id)}>
                        <X className="h-4 w-4" />
                      </Button>
                    </div>
                  </li>
                ))}
              </ul>
              <Pagination
                list="followers"
                currentPage={currentPage.followers}
                setCurrentPage={(page) => setCurrentPage({ ...currentPage, followers: page })}
              />
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  )
}